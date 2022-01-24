import pytest
import requests
import json
import os
import allure
from Basic.yaml_util import YamlUtil



@allure.feature('接口测试')
class Test_runCase():

    # @pytest.mark.parametrize('args',YamlUtil(os.getcwd()+"/API_test_case/获取验证码.yaml").read_yaml())
    # @pytest.mark.parametrize('args',YamlUtil(os.getcwd()+"/API_test_case/").read_case())
    @pytest.mark.parametrize('args',YamlUtil(os.getcwd()+"/API_test_case/").read_case())
    def test_run(self,args):
        print(os.getcwd())

        # allure.dynamic.title('登录')
        # allure.dynamic.description = ('描述')
        # print(args)

        time = args['time']
        # print(time)
        url = args['request']['host']+args['request']['path']
        # print(url)
        headers= args['request']['headers']
        # print(headers)
        data = args['request']['data']
        # print(params)

        #添加操作步骤
        with allure.step(args['name']):
            for i in range(time):
                r = requests.post(url = url,data = data,headers = headers)
                res = r.json()
                print(res)



        print(args['validate']['eq'])

        #断言
        assert str(args['validate']['eq']) in r.text



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

