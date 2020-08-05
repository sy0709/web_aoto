# -*- encoding: utf-8 -*-
"""
@File    : inverstPage_loc.py
@Time    : 2020/7/13 下午 08:05
@Author  : 银子
"""
from selenium.webdriver.common.by import By

class IversPageLocators:

    # 投标金额输入框
    Invest_input = (By.XPATH,"//input[@class='form-control invest-unit-investinput']")
    # 投标按钮
    Invest_button = (By.XPATH, "//button[@class='btn btn-special height_style']")

    # 标可投金额
    bidable_amount = (By.XPATH, "//span[@class='mo_span4']")

    # 投标成功提示弹窗-查看并激活按钮
    activa_button_in_success_popup = (By.XPATH, "//div[text()='投标成功！']/following-sibling::div/button[text()='查看并激活']")




