#用来设置全局变量，供所有的用例来传递参数等
# conftest.py
import pytest
from Basic.log_module import *
import decorator
# 定义一个全局变量，用于存储内容
global_data = {}

@pytest.fixture(scope = "session",autouse=True)
def session_setup_down():
    """
    前置函数
    """
    # 读取日志配置
    log_info = YamlUtil().read_yaml(config_path)
    # print(log_info['log'])

    log = Logger(log_info['log'])
    log.logger.info('----开始执行测试----')
    log.teardown()
    yield
    """
    后置
    """
    log = Logger(log_info['log'])
    log.logger.info('----测试执行结束----')
    log.teardown()

@pytest.fixture(scope = "session")
def set_global_data():
    """
    设置全局变量，用于关联参数
    :return:
    """

    def _set_global_data(key, value):
        global_data[key] = value

    return _set_global_data


@pytest.fixture(scope = "session")
def get_global_data():
    """
    从全局变量global_data中取值
    :return:
    """

    def _get_global_data(key):
        return global_data.get(key)

    return _get_global_data

#环境配置
def pytest_addoption(parser):
    """注册自定义参数 env 到配置对象"""
    parser.addoption(
        "--env",
        dest = "env",
        action="store",
        default="dev",
        help="配置环境变量：dev 测试环境 pro 正式环境 pre预发布环境"
    )

#获取环境配置
@pytest.fixture(scope = "session")
def get_env(request):
    """从配置对象中读取自定义参数的值"""
    return request.config.getoption('env')

#设置环境
@pytest.fixture(scope = "session",autouse=True)
def get_test_data(get_env):
    #读取所有的环境配置
    temp_data = YamlUtil().read_yaml(test_data_path)
    try:
        test_date = temp_data[get_env]
        global_data['test_data'] = test_date
    except:
        print('环境配置错误')

    # return test_date
#log装饰器
def log(type):
    def inner(func):
        def infunc(*args):
            args = args[1:]
            log_args = args[1]
            case_name = log_args['name']
            # 读取日志配置
            log_info = YamlUtil().read_yaml(config_path)
            log = Logger(log_info['log'])
            log.logger.info(f'<{case_name}>用例执行开始')
            log.logger.info(f"接口路径: {log_args['request']['path']}")
            log.logger.info(f"用例名称: {log_args['name']}")
            log.logger.info(f"接口地址: {log_args['request']['host']}{log_args['request']['path']}")
            log.logger.info(f"请求头(headers): {log_args['request']['headers']}")
            log.logger.info(f"请求入参: {log_args['request']['data']}")
            log.teardown()


            func(*args)


            log = Logger(log_info['log'])
            log.logger.info(f"请求响应: 状态码:{log_args['response'].status_code},返回值:{log_args['response'].text}")
            log.logger.info(f"预期结果:{log_args['validate']}")
            log.logger.info(f"实际结果:{log_args['response'].text}")
            if (log_args['case_status']):
                log.logger.info(f"{log_args['name']}: 执行成功！")
            else:
                log.logger.info(f"{log_args['name']}: 执行失败！")

            log.logger.info(f'<{case_name}>用例执行结束')
            log.logger.info("####################")
            log.teardown()
        return decorator.decorator(infunc,func)
    return inner


#设置请求参数装饰器
def set_request_info(type):
    def inner(func):
        def wrapper(*args):
            args = args[1:]
            #设置请求的host
            args[1]['request']['host'] =global_data['test_data']['host']
            func(*args)
            #判断用例状态
            if ( args[1]['case_status']==0):
                pytest.fail("用例指执行失败")

        return decorator.decorator(wrapper,func)
    return inner

