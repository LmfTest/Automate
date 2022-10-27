import pytest
import os
import sys
from Basic.get_path import *
import argparse
if __name__ == '__main__':
    # 设置执行环境dev为测试，pro为正式，pre为预发布
    # 之后只需要在运行run_interface.py文件时增加一个参数(python runfile.py --env=pro),修改env参数就可以切换对应环境
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--env",
        dest="env",
        action="store",
        default="dev", )
    args = parser.parse_args()
    env = args.env

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
