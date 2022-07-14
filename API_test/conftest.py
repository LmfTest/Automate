#用来设置全局变量，供所有的用例来传递参数等
# conftest.py
import pytest
from Basic.log_module import *
# 定义一个全局变量，用于存储内容
global_data = {}
test_args = {}
@pytest.fixture(scope = "function")
def setup_and_down(args):
    """
    前置函数
    """
    case_name = args['name']
    # 读取日志配置
    log_info = YamlUtil().read_yaml(config_path)
    # print(log_info['log'])

    log = Logger(log_info['log'])
    log.logger.info(f'<{case_name}>用例执行开始')
    log.logger.info(f"接口路径: {args['request']['path']}")
    log.logger.info(f"用例名称: {args['name']}")
    log.logger.info(f"接口地址: {args['request']['host']}{args['request']['path']}")
    log.logger.info(f"请求头: {args['request']['headers']}")
    log.logger.info(f"请求入参: {args['request']['data']}")
    log.teardown()
    yield
    """
    后置函数
    """
    log = Logger(log_info['log'])
    log.logger.info(f'<{case_name}>用例执行结束')
    log.logger.info("")
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

