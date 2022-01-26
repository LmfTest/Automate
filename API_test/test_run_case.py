import pytest
import requests
import json
import os
import allure
from Basic.yaml_util import YamlUtil
from Basic.automate_request import Automate_request




@allure.feature('接口测试')
class Test_runCase():

    @pytest.mark.parametrize('args',YamlUtil().read_yaml(os.getcwd()+"/../API_test_case/获取用户信息.yaml"))
    # @pytest.mark.parametrize('args',YamlUtil(os.getcwd()+"/../API_test_case/").read_case())
    # @pytest.mark.parametrize('args',YamlUtil(os.getcwd()+"/API_test_case/").read_case())
    def test_run(self,args):
        # print(os.getcwd())
        allure.dynamic.title(args['name'])
        allure.dynamic.description = ('描述')
        # print(args)

        #
        req = Automate_request(args)

        #添加操作步骤
        with allure.step(args['name']):
            r = req.request_run()
            res = r.json()
            print(res)

        # print(args['validate']['eq'])

        #断言
        try:
            assert str(args['validate']['eq']) in r.text
        except:
            pytest.fail("用例指执行失败")



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
    pytest.main(["-s","-v","./test_run_case.py"])

