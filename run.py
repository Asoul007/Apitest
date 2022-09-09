# -*- coding: utf-8 -*-
# @Time    : 2022/9/3 22:06
# @Author  : Asoul
import unittest
from unittestreport import TestRunner
import os
import os.path
from common.handle_path import REPORT_DIR
# #创建测试套件
# suite = unittest.TestSuite()
# #将测试用例添加到测试套件中
# loader = unittest.TestLoader()
# suite.addTest(loader.loadTestsFromTestCase(TestLogin))
# runner = TestRunner(suite)
suite = unittest.defaultTestLoader.discover(r'D:\PycharmProjects\apitest\test_case')

runner = TestRunner(suite,filename="report.html",
                 report_dir=os.path.join(REPORT_DIR),
                 title='测试报告',
                 tester='王烁',
                 desc="iHO项目测试报告",
                 templates=2)

runner.run()
os.remove(os.path.join(REPORT_DIR,"history.json"))

# url = "https://oapi.dingtalk.com/robot/send?access_token=db17797fdedee20affef032fa7f064a940be3b1198983d5c6dddf8f1f911e317"
# # 发送钉钉通知
# runner.dingtalk_notice(url=url, key='测试')

