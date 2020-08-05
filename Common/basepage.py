from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from Common import logger
import logging
from Common import dir_config

import datetime
import time

class BasePage:
    # 包含了PageObjects当中，用到所有的selenium底层方法。
    # 还可以包含通用的一些元素操作，如alert,iframe,windows...
    # 还可以自己额外封装一些web相关的断言
    # 实现日志记录、实现失败截图
    def __init__(self,driver):
        self.driver = driver

    # 等待元素出现
    def wait_eleVisible(self,loc,img_name,timeout=30,poll_frequency=0.5):
        """

        :param loc: 元素定位表达式 以元组的形式(定位类型、定位元素表达式)
        :param img_name:页面操作的描述（业务操作：在xx页面，操作xx元素、输入、点击）
        :param timeout:超时
        :param poll_frequency:等待元素可见，轮询时间
        :return:none
        """
        logging.info("在 {} 等待元素{}可见".format(img_name,loc))
        try:
            # 起始等待的时间 datatime
            start = datetime.datetime.now()
            WebDriverWait(self.driver,timeout,poll_frequency).until(EC.visibility_of_element_located(loc))
            # 结束等待的时间
            end = datetime.datetime.now()
            logging.info("开始等待时间点：{}，结束等待时间点：{}，等待时长{}".format(start,end,end-start))
        except:
            logging.exception("等待元素可见失败：")
            # 截图 -哪一个页面-哪一个操作导致的失败+当前时间
            self.save_web_screenshot(img_name)
            raise

    # 查找一个元素
    def get_element(self,loc,img_name=""):
        """

        :param loc:元素定位表达式 以元组的形式(定位类型、定位元素表达式)
        :param img_name:页面操作的描述（业务操作：在xx页面，操作xx元素、输入、点击）
        :return:
        """
        logging.info("在{}，查找元素{}".format(img_name,loc))
        try:
            # 查找元素
            ele = self.driver.find_element(*loc)
        except:
            # 日志
            logging.exception("查找元素失败：")
            # 截图
            self.save_web_screenshot(img_name)
            raise
        else:
            return ele

    # 点击操作
    def click_element(self,loc,img_name,timeout=30,poll_frequency=0.5):
        """

        :param loc:元素定位表达式 以元组的形式(定位类型、定位元素表达式)
        :param img_name:页面操作的描述（业务操作：在xx页面，操作xx元素、输入、点击）
        :param timeout:
        :param poll_frequency:
        :return:
        """
        # 等待元素可见
        self.wait_eleVisible(loc,img_name,timeout,poll_frequency)
        # 查找元素
        ele = self.get_element(loc,img_name)
        logging.info("在{}，点击元素{}".format(img_name,loc))
        try:
            ele.click()
        except:
            logging.exception("点击操作失败：")
            # 截图
            self.save_web_screenshot(img_name)
            raise

    # 输入操作
    def input_text(self,loc,value,img_name,timeout=30,poll_frequency=0.5):
        """

        :param loc: 元素定位表达式 以元组的形式(定位类型、定位元素表达式)
        :param value: 代表要输入的内容
        :param img_name: 页面操作的描述（业务操作：在xx页面，操作xx元素、输入、点击）
        :param timeout:
        :param poll_frequency:
        :return:
        """
        # 等待元素可见
        self.wait_eleVisible(loc,img_name,timeout,poll_frequency)
        # 查找元素
        ele = self.get_element(loc,img_name)
        # 操作
        logging.info("在{}，给{}元素，输入：{}".format(img_name,loc,value))
        try:
            ele.send_keys(value)
        except:
            logging.exception("元素输入失败：")
            # 截图
            self.save_web_screenshot(img_name)
            raise

    # 获取元素文本内容
    def get_element_text(self,loc,img_name,timeout=30,poll_frequency=0.5):
        """

        :param loc: 元素定位表达式 以元组的形式(定位类型、定位元素表达式)
        :param img_name: 页面操作的描述（业务操作：在xx页面，操作xx元素、输入、点击）
        :param timeout:
        :param poll_frequency:
        :return:
        """

        # 等待元素可见
        self.wait_eleVisible(loc,img_name,timeout,poll_frequency)
        # 查找元素
        ele = self.get_element(loc,img_name)
        # 操作
        try:
            text = ele.text
            logging.info("在{}，获取元素：{}的文本:{}".format(img_name,loc,text))
        except:
            logging.exception("获取元素文本内容失败：")
            # 截图
            self.save_web_screenshot(img_name)
            raise
        else:
            return text

    # 获取元素属性值
    def get_element_attr(self,loc,attr_name,img_name,timeout=30,poll_frequency=0.5):
        """

        :param loc: 元素定位表达式 以元组的形式(定位类型、定位元素表达式)
        :param attr_name: 属性名称，get_attribute(属性名)，通过属性名获取属性值
        :param img_name: 页面操作的描述（业务操作：在xx页面，操作xx元素、输入、点击）
        :param timeout:
        :param poll_frequency:
        :return:
        """
        # 等待元素可见
        self.wait_eleVisible(loc,img_name,timeout,poll_frequency)
        # 查找元素
        ele = self.get_element(loc,img_name)
        # 操作
        try:
            attr_value = ele.get_attribute(attr_name)
            logging.info("在{}，获取元素：{}的属性{}值：{}".format(img_name,loc,attr_name,attr_value))
        except:
            logging.exception("获取元素属性值失败：")
            # 截图
            self.save_web_screenshot(img_name)
            raise
        else:
            return attr_value

    # 截图并保存
    def save_web_screenshot(self,img_name):
        """

        :param img_name: 页面操作的描述（业务操作：在xx页面，操作xx元素:、输入、点击）
        :return:
        """

        # 函数接收以时间元组，并返回以可读字符串表示的当地时间，格式由参数format决定
        # 获取当前时间
        now = time.strftime("%Y-%m-%d %H_%M_%S")
        #  页面_功能_时间.png
        #  img_name是传入的自定义截图名称，在xx页面，操作xx功能发生错误截图
        file_name = "{}_{}.png".format(img_name,now)
        try:
            self.driver.save_screenshot(dir_config.screenshot_dir+"/"+file_name)
            logging.info("截图成功，图标保存在{}".format(dir_config.screenshot_dir+"/"+file_name))
        except:
            logging.exception("截图失败")

# windows切换

# iframe切换

# select下拉列表

# 上传操作
if __name__ == '__main__':
    url = "https://www.baidu.com/"
    from selenium import webdriver
    driver = webdriver.Chrome()
    driver.get(url)
    loc = ("id","kw")
    click_loc = ("id","su")
    value = BasePage(driver).get_element_attr(click_loc,"class","百度首页_获取属性值")
    value2= BasePage(driver).get_element_text(click_loc,"百度首页_获取文本内容")

    print(value)
    print(value2)

    BasePage(driver).input_text(loc,"苹果","百度页面输入")
    BasePage(driver).click_element(click_loc,"百度首页_点击搜索按钮")
