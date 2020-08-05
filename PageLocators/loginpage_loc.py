# -*- encoding: utf-8 -*-
"""
@Time    : 2020/7/8 下午 09:45
@Author  : 银子
"""
from selenium.webdriver.common.by import By
class LoginPageLocators:

    #登录页面元素定位

    #用户名输入框
    userName = (By.XPATH,"//input[@name='phone']")
    #密码输入框
    pwd = (By.XPATH,"//input[@name='password']")
    #登录按钮
    #login_but = (By.CLASS_NAME,"btn btn-special")
    login_but = (By.XPATH,"//button[text()='登录']")
    #记住手机号单选框
    remember_phone = (By.XPATH, "//input[@name='remember_me']")
    #注册
    register_enter = (By.XPATH, '//a[@href="/Index/reg.html"]')
    #忘记密码"
    forget_pwd = (By.XPATH,"//a[@href='/Index/find_pwd.html']")
    #错误提示框--登录区域
    erroMsg_from_loginPhone = (By.CLASS_NAME,"form-error-info")
    #错误提示框--登录页面中间
    erroMsg_from_login_pageCotent = (By.CLASS_NAME,"layui-layer-content")

    #找回密码页面元素
    find_back_passwd_tittle = (By.XPATH,"//div[text()='找回密码']")

    #注册页面元素
    register_page_tittle = (By.XPATH,"//div[text()='注册']")






