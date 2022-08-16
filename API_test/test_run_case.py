import pytest
import requests
import json
import os
import allure
from Basic.yaml_util import YamlUtil
from Basic.automate_request import Automate_request
from Basic.log_module import Logger
from Basic.get_path import *





@allure.feature('接口测试')
class Test_runCase():

    @pytest.mark.parametrize('args',YamlUtil().read_yaml(os.path.join(case_dir, "testcase.yaml")))
    # @pytest.mark.parametrize('args',YamlUtil(os.getcwd()+"/../API_test_case/").read_case())
    # @pytest.mark.parametrize('args',YamlUtil(case_dir).read_case())

    def test_run(self,args,setup_and_down):

        allure.dynamic.title(args['name'])
        allure.dynamic.description = ('描述')

        #用例状态,默认失败
        #case_status = 0
        #添加日志
        # 读取日志配置
        log_info = YamlUtil().read_yaml(config_path)
        log = Logger(log_info['log'])
        #实例化请求对象
        req = Automate_request(args)
        #添加操作步骤
        with allure.step(args['name']):
            r = req.request_run()
            res = r.json()
            log.logger.info(f"请求响应: 状态码:{r.status_code},返回值:{res}")
            log.logger.info(f"预期结果:{args['validate']}")
            log.logger.info(f"实际结果:{res}")


        # print(args['validate']['eq'])


        #断言
        try:
            assert str(args['validate']['eq']) in r.text
            case_status = 1
            log.logger.info(f"{args['name']}: 执行成功！")
            # log.teardown()

        except:

            log.logger.info(f"{args['name']}: 执行失败！")
            log.teardown()      #pytest.fail会让用例直接结束，所以log.teardown要在此之前
            pytest.fail("用例指执行失败")

        log.teardown()






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


