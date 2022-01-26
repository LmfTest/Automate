import os
import hashlib
import json
import requests


class Automate_request:

    def __init__(self,*args):
        self.args = args[0]
        # self.args = dict(self.args)

    #提取基本信息
    def request_baseInfo(self):

        self.url = self.args['request']['host'] + self.args['request']['path']
        # print(url)

        #判空给空字典
        try:
            if type(self.args['request']['headers']) == dict:
                self.headers = self.args['request']['headers']
            else:
                self.args['request']['headers'] = {}
        except:
            self.args['request']['headers'] = {}
        finally:
            self.headers = self.args['request']['headers']

        # print("self.headers:"+str(self.headers))

        # print(headers)
        self.data = self.args['request']['data']
        # print(data)
        self.method = self.args['request']['method']

    # 整理数据，设定默认值
    def sorting_data(self):
        #将请求次数转化成整数，小于1或者无值时赋予默认值1
        try:
            if self.args['times'] and self.args['times']>1:
                self.args['times'] = int(self.args['times'])
            else:
                self.args['times'] = 1
        except Exception as e:
            print(e)
            # self.args['times'] = 1
            self.args.update(times=1)

        #验证码md5加密
        try:
            if self.args['apiVersion'] == 'v2':
                if self.args['request']['data']['verify_code']:
                    self.args['request']['data']['verify_code'] = hashlib.md5(str(self.args['request']['data']['verify_code']).encode(encoding='UTF-8')).hexdigest()
        except Exception as e:
            print(e)

        #token为空时，设定默认token
        try:
            if not self.args['request']['headers']['Authorization']:
                self.args['request']['headers']['Authorization'] = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2NvdW50X2lkIjowLCJlbnYiOiJkZXYiLCJleHAiOjE2NDU2MDEwMzgsIm9wZW5pZCI6IiIsInBob25lIjoidjMxODIzMDE4MDIiLCJzZXNzaW9uX2tleSI6IiIsInRva2VuX3R5cGUiOjUsInVzZXJfaWQiOjgyNX0.RNog12dTCqH-c4SYGpTkh_v-DL8dq1mPxbbIDh_c0Jg"
        except Exception as e:
            default_authorization = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2NvdW50X2lkIjowLCJlbnYiOiJkZXYiLCJleHAiOjE2NDU2MDEwMzgsIm9wZW5pZCI6IiIsInBob25lIjoidjMxODIzMDE4MDIiLCJzZXNzaW9uX2tleSI6IiIsInRva2VuX3R5cGUiOjUsInVzZXJfaWQiOjgyNX0.RNog12dTCqH-c4SYGpTkh_v-DL8dq1mPxbbIDh_c0Jg"
            a={
                "request":{
                    "headers":{
                        "Authorization":default_authorization
                    }
                }
            }
            # self.args.update(a)
            self.args['request']['headers']['Authorization'] = default_authorization
        return self.args

    #发送请求
    def request_run(self):

        self.request_baseInfo()
        self.sorting_data()

        if self.method.upper() == "POST":
            for i in range(self.args['times']):
                res = requests.post(url = self.url,data = self.data,headers = self.headers)
            return res
        elif self.method.upper() == "GET":
            for i in range(self.args['times']):
                res = requests.get(url=self.url, data=self.data, headers=self.headers)
            return res