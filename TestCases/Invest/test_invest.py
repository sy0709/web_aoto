# -*- encoding: utf-8 -*-
"""
@File    : test_invest.py
@Time    : 2020/7/13 下午 08:01
@Author  : 银子
"""
import pytest

from selenium import webdriver
import logging
from Common import logger
from PageObjects.login_page import LoginPage
from PageObjects.index_page import IndexPage
from PageObjects.inverst_page import InverstPage
from PageObjects.user_details_page import UserDetailsPage

from TestDatas.login_datas.commonDatas import CommonDatas as cd

import time


@pytest.fixture()
def init(init_driver_fun):
    logging.info("实例化PO页面对象")
    LoginPage(init_driver_fun).login(*cd.invest_user)
    ip = InverstPage(init_driver_fun)
    udp = UserDetailsPage(init_driver_fun)
    ixp = IndexPage(init_driver_fun)
    yield init_driver_fun,ip,udp,ixp


class TestInverst():

    """
    步骤
        1、首页-选竞标中第一个
        2、标页面-获取标余额
        3、标页面-获取用户余额
        4、标页面-输入投资金额，点击投标
        5、投票成功弹窗-点击查看并激活"


        断言
        "1、帐户少2000
        1.1、获取帐户金额
        2、标可投金额少2000
        断言：投前余额-投后余额=2000
        2.1、返回上一页面（标页面）刷新页面，获取标可投金额
        断言：（投前标额-投后标额）*10000=2000"


    """
    # def setUp(self) -> None:
    #     logging.info("打开浏览器")
    #     self.driver = webdriver.Chrome()
    #     logging.info("最大化窗口")
    #     self.driver.maximize_window()
    #     logging.info("输入登录页面网址")
    #     self.driver.get(cd.login_url)
    #     logging.info("登陆操作")
    #     logging.info("实例化PO页面对象")
    #     LoginPage(self.driver).login(*cd.invest_user)
    #     self.ip = InverstPage(self.driver)
    #     self.udp = UserDetailsPage(self.driver)
    #
    # def tearDown(self) -> None:
    #     self.driver.quit()

    # 正向流程 投资成功 选择首页第一个标 输入2000
    def test_success_bid(self,init):
        # 选择首页第一个标（状态为竞标中），点击"抢投标"按钮
        init[3].choose_the_first_bid()

        time.sleep(2)

        # 获取投前标额
        money_before_bid = float(init[1].get_bid_money())
        logging.info('投前标额{}'.format(money_before_bid))

        # 获取用户投标前的可用余额
        user_money_before_invest = float(init[1].get_user_money())
        logging.info('用户投标前{}'.format(user_money_before_invest))

        # 标页面-输入投资金额，点击投标
        init[1].user_invest(cd.invest_money)
        logging.info('-------------------成功输入投资金额----------------------')

        # 投票成功弹窗-点击查看并激活"
        init[1].click_activa_button_in_success_popup()

        # 帐户少2000 获取帐户金额
        user_money_after_invest =float(init[2].get_user_money())
        logging.info('用户投标后{}'.format(user_money_after_invest))

        # 返回上一页面，刷新页面
        init[0].back()
        init[0].refresh()

        # 获取投资后标可投金额
        money_after_bid = float(init[1].get_bid_money())
        logging.info('投后标额{}'.format(money_after_bid))

        logging.info("断言")
        # 断言：用户投前余额-投后余额=2000
        assert int(user_money_before_invest - user_money_after_invest) == cd.invest_money
        # 断言：（投前标额-投后标额）*10000=2000"
        assert int((money_before_bid - money_after_bid)*10000) == cd.invest_money


# if __name__ == '__main__':
#     pytest.main('-s','-v')









