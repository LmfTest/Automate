# coding=utf-8
import logging
import time
import os
from Basic.get_path import *
from Basic.yaml_util import YamlUtil


class Logger(object):

    def __init__(self, log_info):
        self.log_file = log_file           #日志路径
        # self.log_file = os.path.join(log_dir, '%s.log'%time.strftime('%Y-%m-%d'))  # 日志路径
        self.level = log_info['log_level']          #文件日志等级
        self.format = log_info['log_format']        #文件日志格式
        # 创建一个logger
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        # 创建一个handler，用于写入日志文件
        self.fh = logging.FileHandler(self.log_file, 'a', encoding='utf-8')
        self.fh.setLevel(logging.DEBUG)
        # 再创建一个handler，用于输出到控制台
        self.ch = logging.StreamHandler()
        self.ch.setLevel(logging.DEBUG)
        # 定义handler的输出格式
        formatter = logging.Formatter(self.format)
        self.fh.setFormatter(formatter)
        self.ch.setFormatter(formatter)
        # 给logger添加handler
        self.logger.addHandler(self.fh)
        self.logger.addHandler(self.ch)




    def teardown(self):
        self.logger.removeHandler(self.ch)
        self.logger.removeHandler(self.fh)
        # 关闭打开的文件
        self.fh.close()

    def __print_console(self, level, *message):

        # 记录一条日志
        if level == 'info':
            self.logger.info(message)
        elif level == 'debug':
            self.logger.debug(message)
        elif level == 'warning':
            self.logger.warning(message)
        elif level == 'error':
            self.logger.error(message)
        # self.logger.removeHandler(ch)
        # self.logger.removeHandler(fh)
        # 关闭打开的文件


    def debug(self, message):
        self.__print_console('debug', message)

    def info(self, message):
        self.__print_console('info', message)

    def warning(self, message):
        self.__print_console('warning', message)

    def error(self, message):
        self.__print_console('error', message)

    def log(self,message):

        if self.level == 'info':
            self.logger.info(message)
        elif self.level == 'debug':
            self.logger.debug(message)
        elif self.level == 'warning':
            self.logger.warning(message)
        elif self.level == 'error':
            self.logger.error(message)




if __name__ == "__main__":

    #读取日志配置
    log_info = YamlUtil().read_yaml(config_path)
    # print(log_info['log'])
    log = Logger(log_info['log'])
    # log.log("正常信息")
    log.logger.info('111')



