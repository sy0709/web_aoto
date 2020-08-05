# -*- encoding: utf-8 -*-
"""
@File    : index_page.py
@Time    : 2020/7/8 下午 10:56
@Author  : 银子
"""

from time import sleep
from PageLocators.indexPage_loc import IndexPageLocators as loc
from Common.basepage import BasePage


class IndexPage(BasePage):
    """实现登录页面功能"""

    # 获取退出按钮
    def index_exit(self):
        try:
            self.wait_eleVisible(loc.exit_but,"首页_等待退出按钮出现")
        except:
            return False
        else:
            return True

    # 选择首页第一个标
    def choose_the_first_bid(self):
        self.click_element(loc.bid_button,"首页_点击第一个抢投标按钮")




