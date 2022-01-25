import os
import hashlib

class Request_info:

    def __init__(self,*args):
        self.args = args[0]

    #整理数据，设定默认值
    def sorting_data(self):
        #将请求次数转化成整数，小于1或者无值时赋予默认值1
        try:
            if self.args['times'] and self.args['times']>1:
                self.args['times'] = int(self.args['times'])
            else:
                self.args['times'] = 1
        except Exception as e:
            print(e)
            self.args['times'] = 1

        #验证码md5加密
        try:
            if self.args['apiVersion'] == 'v2':
                if self.args['request']['data']['verify_code']:
                    self.args['request']['data']['verify_code'] = hashlib.md5(str(self.args['request']['data']['verify_code']).encode(encoding='UTF-8')).hexdigest()
        except Exception as e:
            print(e)

        return self.args
