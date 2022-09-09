"""
====================================
@Author:Asoul
@Email:blink_wang@163.com
@FileName:log_handler.py
@DateTime:2022/8/27 16:05
====================================
"""
from common.handle_path import LOG_DIR
import os.path
import logging
class HandlerLog:
    @staticmethod
    def create_log():
        """第一步创建收集器"""
        # 创建收集器
        # global logger
        logger = logging.getLogger('logger')
        # 设置收集等级
        logger.setLevel("INFO")
        """第二步创建输出渠道"""
        # 创建输出渠道
        fh = logging.FileHandler(os.path.join(LOG_DIR,"logging.log") , mode='a', encoding='utf-8')
        # 设置输出渠道等级
        fh.setLevel('INFO')
        """第三步相互绑定"""
        # 收集器绑定输出渠道
        logger.addHandler(fh)

        # 设置输出格式
        lf = logging.Formatter('%(asctime)s - [%(filename)s-->line:%(lineno)d] - %(levelname)s: %(message)s')
        fh.setFormatter(lf)

        #返回日志收集器
        return logger

#@staticmethod方法可以直接用类调用方法
log = HandlerLog.create_log() #如果实例方法参数带有self就不能这样调用，会报错，必须先实例化一个对象，然后再调用

#实例方法参数带有self
# hc = HandlerLog() #带有self需先实例化对象，不带self可以用@staticmethod静态方法
# log = hc.create_log()

