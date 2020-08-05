import logging
from scripts.handle_config import conf
from scripts.constants import LOGS_DIR


class HandleLogger:
    '''
    定义一个日志处理类
    '''
    def __init__(self):
        self.case_logger = logging.getLogger(conf.get_value('log', 'logger_name'))  # 创建一个日志收集器

        self.case_logger.setLevel(conf.get_value('log', 'level_debug'))  # 指定日志收集器的日志等级

        console_handle = logging.StreamHandler()  # 定义一个控制台输出渠道
        file_handle = logging.FileHandler(LOGS_DIR + '\AutoTest.log', encoding='utf-8')  # 定义一个文件输出渠道

        console_handle.setLevel(conf.get_value('log', 'level_error'))  # 设置控制台输出渠道的日志级别为ERROR
        file_handle.setLevel(conf.get_value('log', 'level_info'))  # 设置文件输出渠道的日志级别为INFO

        simple_formatter = logging.Formatter(conf.get_value('log', 'simple_formatter'))  # 定义简洁类型日志格式
        verbose_formatter = logging.Formatter(conf.get_value('log', 'verbose_formatter'))  # 定义详细类型日志格式

        console_handle.setFormatter(simple_formatter)  # 控制台显示简洁的日志
        file_handle.setFormatter(verbose_formatter)  # 文件中显示详细的日志

        # 将日志收集器与输出渠道对接
        self.case_logger.addHandler(console_handle)
        self.case_logger.addHandler(file_handle)

    def get_case_logger(self):  # 获取日志收集器
        return self.case_logger


do_case = HandleLogger()  # 创建一个日志对象
logger = do_case.get_case_logger()  # 创建一个日志器方法