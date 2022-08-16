import pytest
import os
from Basic.get_path import *

if __name__ == '__main__':

    env = "dev"
    # pytest.main(['-vs'])
    # pytest.main(['-vs','-n 2','--reruns=2' ,'ios_testcase/test_login.py','ios_testcase/test_createOrder.py'])
    # pytest.main(['-v@pytest.mark.run(order = 1)s','-n 2','ios_testcase/test_login.py','ios_testcase/test_createOrder.py'])

    # print(os.getcwd())
    #执行测试用例
    pytest.main([f'--env={env}'])
    # pytest.main(["-s", "-v", "../API_test/test_run_case.py"])
    #生成测试报告
    os.system(f'allure generate ./temp -o {report_dir} --clean')

    # 清空json临时测试报告
    os.system('rm -rf ./temp/')
