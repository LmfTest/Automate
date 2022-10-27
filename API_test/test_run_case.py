import pytest
import requests
import json
import os
import allure
from Basic.yaml_util import YamlUtil
from Basic.automate_request import Automate_request
from Basic.log_module import Logger
from Basic.get_path import *
from conftest import *



@allure.feature('接口测试')
class Test_runCase():

    @pytest.mark.parametrize('args',YamlUtil().read_yaml(os.path.join(case_dir, "testcase.yaml")))
    # @pytest.mark.parametrize('args',YamlUtil(os.getcwd()+"/../API_test_case/").read_case())
    # @pytest.mark.parametrize('args',YamlUtil(case_dir).read_case())

    @set_request_info(1)
    @log(config_path)
    def test_run(self,args):

        allure.dynamic.title(args['name'])
        allure.dynamic.description = ('描述')

        #用例状态,默认失败

        #实例化请求对象
        req = Automate_request(args)
        #添加操作步骤
        with allure.step(args['name']):
            r = req.request_run()
            args['response'] = r

        #断言
        try:
            assert str(args['validate']['eq']) in r.text
            args['case_status'] = 1

        except:
            args['case_status'] = 0
            # pytest.fail("用例指执行失败")
            # pytest.xfail("用例指执行失败")










        #截图

        # try:
        #     assert str(args['validate']['eq']) in r.text
        #
        # except:
        #     pytest.fail('用例指执行失败')
        #
        # finally:
        #     allure.attach(self.web.driver.get_screenshot_as_png(),'运行结果截图',allure.attachment_type.PNG())
        #
        #
        #

if __name__ == '__main__':


    print(os.getcwd())

    pytest.main(["./test_run_case.py"])


