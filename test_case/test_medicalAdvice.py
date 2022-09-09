"""
====================================
@Author:Asoul
@Email:blink_wang@163.com
@FileName:test_medicalAdvice.py
@DateTime:2022/9/8 9:44
@Code Description:
====================================
"""
from test_case.test_login import Test_Login, base_url, header
import os
import requests
import ddt
import unittest
from common.handle_excel import HandleXls
from common.handle_path import DATA_DIR
from common import myddt
from common.handle_log import log
import json
@myddt.ddt
class Test_Advice(unittest.TestCase):
    excel = HandleXls(os.path.join(DATA_DIR, "testcases.xlsx"), "advices")
    case_data = excel.read_excel()

    @myddt.data(*case_data)
    def test_advice(self, case):
    # 准备用例
        expected = eval(case["expected"])
        data = eval(case["data"])
        method = case["method"]
        url = os.path.join(base_url,case["url"])
    #获取实际结果
        response = requests.request(method,url=url,json=data,headers=header)
        res =response.json()
        print("预期结果：",expected)
        print("实际结果：",res)
    #断言
        try:
            self.assertEqual(expected["code"],res["code"])
            self.assertEqual(expected["success"],res["success"])
        except AssertionError as e:
            log.error(case["title"])
            log.exception(e)
            raise e
        else:
            log.info(case["title"])
