"""
====================================
@Author:Asoul
@Email:blink_wang@163.com
@FileName:demo1.py
@DateTime:2022/9/5 19:33
@Code Description:
====================================
"""
# import json
#
# # Python 字典类型转换为 JSON 对象
# data = {
#     'no': 1,
#     'name': 'Runoob',
#     'url': 'http://www.runoob.com'
# }
#
# json_str = json.dumps(data)
# print("Python 原始数据：", repr(data))
# print("JSON 对象：", json_str)
from jsonpath import jsonpath
from common.handle_request import ApiRequest
import requests
class Test_All:

    def login_test(self):
        """登录："""

        url="http://192.168.1.211:8088/auth-app/auth/login"
        headers = {"Content-Type": "application/json"}
        data= {"code":"48248060","password":"w123456"}
        response = requests.post(url=url,json=data,headers=headers)
        res = response.json()
        # token=res['data']['access_token']
        # jsonpath提取出来的是列表，需要加[0]
        token = jsonpath(res,"$..access_token")[0]
        token ="Bearer"+" "+token
        print(res)
        print(token)



if __name__ == '__main__':
    ls = Test_All()
    ls.login_test()