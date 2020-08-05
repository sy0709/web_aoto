# -*- encoding: utf-8 -*-
"""
@Time    : 2020/7/8 下午 09:45
@Author  : 银子
"""
from selenium.webdriver.common.by import By


class IndexPageLocators:

    # 登录成功后显示"退出"按钮
    exit_but = (By.XPATH,"//a[text()='退出']")

    # 抢投标按钮
    bid_button = (By.XPATH,"//a[text()='抢投标']")



