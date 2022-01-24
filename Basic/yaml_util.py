import yaml
import glob


class YamlUtil:

    # def __init__(self,yaml_file):
    #
    #     self.yaml_file = yaml_file

    def __init__(self, *args):

        if len(args):
            self.yaml_file = args[0]
        else:
            self.yaml_file = ''

    # 获取文件夹下所有的yaml文件
    def get_yamlFile(self, dir_path):

        yamls = glob.glob(dir_path + "/*.yaml")
        return yamls

    # 读取yaml文件
    def read_yaml(self, file):
        """
        读取yaml,对yaml反序列化，就是把yaml格式转化成dict格式
        :return:
        """
        with open(file, encoding='utf-8') as f:
            value = yaml.load(f, Loader=yaml.CFullLoader)

            # print(value,type(value))
            return value

    # 读取文件夹下所有的yaml文件，拼接所有的用例
    def read_case(self):

        cases = []
        yamls = self.get_yamlFile(self.yaml_file)

        for yaml in yamls:
            values = self.read_yaml(yaml)
            for value in values:
                cases.append(value)

        return cases

#测试代码
if __name__ == '__main__':
    v = YamlUtil().read_yaml("../API_test_case/获取验证码.yaml")
    print(v)
    print(len(v))

    # v2 = get_yamlFile("./")
    # print(v2)
    cases = YamlUtil("./").read_case()
    print(cases)
    print(len(cases))
