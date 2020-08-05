# -*- encoding: utf-8 -*-
"""
@File    : login_page.py
@Time    : 2020/7/8 下午 10:56
@Author  : 银子
"""

from PageLocators.loginpage_loc import LoginPageLocators as loc
from Common.basepage import BasePage


class LoginPage(BasePage):
    """实现登录页面功能"""

    # 登录
    def login(self,phone,passwd,reme=True):

        # 输入帐号
        # self.driver.find_element(*loc.userName).send_keys(phone)
        self.input_text(loc.userName,phone,"登录页面_输入帐号")

        # 输入密码
        # self.driver.find_element(*loc.pwd).send_keys(passwd)
        self.input_text(loc.pwd,passwd,"登录页面_输入密码")

        # 记住手机号
        if reme != True:
            #self.driver.find_element(*loc.remember_phone).click()
            self.click_element(loc.remember_phone,"登录页面_记住手机号")

        # 点击登录
        # WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(loc.login_but))
        # self.driver.find_element(*loc.login_but).click()
        self.click_element(loc.login_but,"登录页面_点击登录")

    def login_error_msg(self):

        return self.get_element_text(loc.erroMsg_from_loginPhone,"登录页面_获取登录区域提示信息")

    def page_content_error_msg(self):

        return self.get_element_text(loc.erroMsg_from_login_pageCotent,"登录页面_获取登录页面中间提示信息")

    def check_register_enter(self):

        return self.get_element_text(loc.register_page_tittle,"注册页面_获取注册页面标题")

    def click_register_enter(self):
        self.click_element(loc.register_enter,"登录页面_点击注册按钮")










if __name__ == '__main__':
    from selenium import webdriver
    driver = webdriver.Chrome()
    driver.get('http://120.78.128.25:8765/Index/login.html')
    LoginPage(driver).login('18684720553','python',False)








