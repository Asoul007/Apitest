"""
====================================
@Author:Asoul
@Email:blink_wang@163.com
@FileName:test_login.py
@DateTime:2022/9/5 9:52
@Code Description:
====================================
"""
from jsonpath import jsonpath
from common.handle_request import ApiRequest
import requests
# class Test_All:
#
#     def login_test(self):
#         """登录："""#
#         url="http://192.168.1.211:8088/auth-app/auth/login"
#         headers = {"Content-Type": "application/json"}
#         data= {"code":"48248060","password":"w123456"}
#         response = requests.post(url=url,json=data,headers=headers)
#         res = response.json()
#         # token=res['data']['access_token']
#         # jsonpath提取出来的是列表，需要加[0]
#         token = jsonpath(res,"$..access_token")[0]
#         token ="Bearer"+" "+token
#         print(res)
#         print(token)
#
# if __name__ == '__main__':
#     ls = Test_All()
#     ls.login_test()



from common.handle_request import ApiRequest
from common.handle_excel import HandleXls
from common import myddt
import unittest
from common.handle_log import log
import unittestreport
import requests
from common.handle_path import DATA_DIR
from jsonpath import jsonpath
import json
import time
import ddt
import os.path
# class Test_All:
#
#     def login_test(self):
#         """登录："""
#         ar = ApiRequest()
#         url="http://192.168.1.211:8088/auth-app/auth/login"
#         header = {"Content-Type": "application/json"}
#         data= {"code":"48248060","password":"w123456"}
#         res = ar.post_method(url=url,data=data,header=header)
#         token = jsonpath(res,"$..access_token")
#         res=ar.run_method(method='post',url=url,data=data,header=header)
#         print(res,type(res))
#         print(token)
#         try:
#             self.assertEqual(res,token)
#         except Exception as e:
#             raise e
#
# if __name__ == '__main__':
#     ls = Test_All()
#     ls.login_test()

# base_url = "http://192.168.1.211:8088/"
# header ={"Content-Type": "application/json"}
# @myddt.ddt
# class Test_Login(unittest.TestCase):
#     """登录成功"""
#     excel=HandleXls(os.path.join(DATA_DIR,"testcases.xlsx"),'login')
#     case_data=excel.read_excel()
#
#     @myddt.data(*case_data)
#     def test_login(self,case):
#         # 1.准备用例数据
#         global base_url
#         expected=eval((case['expected']))
#         # 入参
#         url = os.path.join(base_url,case['url'])
#         params=eval(case['data'])
#         method=case['method']
#         # 2.调用函数，获取实际结果
#         # ar = ApiRequest()
#         response =requests.request(method,url=url,json=params,headers=header)
#         res =response.json()
#         print("预期结果：",expected)
#         print("实际结果：",res)
#         # 3.对比
#         try:
#             self.assertEqual(expected["code"],res["code"])
#             self.assertEqual(expected["success"], res["success"])
#         except AssertionError as e:
#             log.error(case['title'])
#             log.exception(e)
#             raise e
#         else:
#             log.info(case['title'])

base_url = "http://192.168.1.211:8088/"
headers ={"Content-Type": "application/json"}

@myddt.ddt
class Test_Login(unittest.TestCase):
    """登录成功"""
    excel=HandleXls(os.path.join(DATA_DIR,"testcases.xlsx"),'login')
    case_data=excel.read_excel()

    @myddt.data(*case_data)
    def test_login(self,case):
        # 1.准备用例数据
        global base_url
        expected=eval((case['expected']))
        # 入参
        method = case['method']
        url = os.path.join(base_url,case['url'])
        params=eval(case['data'])
        # 2.调用函数，获取实际结果
        # ar = ApiRequest()
        response =requests.request(method=method,url=url,json=params,headers=headers)
        res =response.json()
        token = jsonpath(res,"$..access_token")[0]
        token = "Bearer"+" "+token
        print(token)
        print("预期结果：",expected)
        print("实际结果：",res)
        # 3.断言
        try:
            self.assertEqual(expected["code"],res["code"])
            self.assertEqual(expected["success"], res["success"])
        except AssertionError as e:
            log.error(case['title'])
            log.exception(e)
            raise e
        else:
            log.info(case['title'])










