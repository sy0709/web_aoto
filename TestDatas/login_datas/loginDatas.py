# -*- encoding: utf-8 -*-
"""
@File    : loginDatas.py
@Time    : 2020/7/9 上午 11:39
@Author  : 银子
"""
#正常登录
#正常的用户名，密码
class LoginDatas:

    true_data = [{'phone':'18684720553','passwd':'python'}]

    #异常登录
    #手机号格式不正确 (手机号为空、少于11位，多于11位，不在号码段）
    #手机号与密码均不正确
    false_phtone =[{'phone':'','passwd':'python','expectation':'请输入手机号'},
                   {'phone':'1868472055','passwd':'python','expectation':'请输入正确的手机号'},
                   {'phone':'186847205531','passwd':'python','expectation':'请输入正确的手机号'},
                   {'phone':'11184720553','passwd':'python','expectation':'请输入正确的手机号'}]

    # 异常登录
    # 密码格式不正确 (错误密码，密码少于6位）
    false_passwd = [{'phone': '18684720553', 'passwd': '111111','expectation':'帐号或密码错误!'},
                    {'phone': '18684720553', 'passwd': 'pytho','expectation':'帐号或密码错误!'}]

    #密码为空
    empty_passwd = [{'phone': '18684720553', 'passwd': '', 'expectation': '请输入密码'}]



