#用来设置全局变量，供所有的用例来传递参数等
# conftest.py
import pytest
from Basic.log_module import *
import decorator
# 定义一个全局变量，用于存储内容
global_data = {}
test_args = {}
@pytest.fixture(scope = "function")
def setup_and_down(args,get_test_data):
    """
    前置函数
    """
    case_name = args['name']
    args['request']['host'] = get_test_data['host']
    # 读取日志配置
    log_info = YamlUtil().read_yaml(config_path)
    # print(log_info['log'])

    log = Logger(log_info['log'])
    log.logger.info(f'<{case_name}>用例执行开始')
    log.logger.info(f"接口路径: {args['request']['path']}")
    log.logger.info(f"用例名称: {args['name']}")
    log.logger.info(f"接口地址: {args['request']['host']}{args['request']['path']}")
    log.logger.info(f"请求头(headers): {args['request']['headers']}")
    log.logger.info(f"请求入参: {args['request']['data']}")
    log.teardown()
    yield
    """
    后置函数
    """
    log = Logger(log_info['log'])
    log.logger.info(f'<{case_name}>用例执行结束')
    log.logger.info("####################")
    log.teardown()


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
@pytest.fixture(scope= "session")
def get_env(request):
    """从配置对象中读取自定义参数的值"""
    return request.config.getoption('env')

#设置环境
@pytest.fixture(scope= "session")
def get_test_data(get_env):
    #读取所有的环境配置
    temp_data = YamlUtil().read_yaml(test_data_path)
    try:
        test_date = temp_data[get_env]
    except:
        print('环境配置错误')

    return test_date

def log1(file):
    print(file)
    def inner(func):
        def infunc(*args):
            print("执行log函数开始")
            print(args)
            args = args[1:]
            print(args)
            func(*args)
            print("执行log函数结束")
        return decorator.decorator(infunc,func)
    return inner
