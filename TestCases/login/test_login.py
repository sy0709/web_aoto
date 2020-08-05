# -*- encoding: utf-8 -*-
"""
@File    : test_login.py
@Time    : 2020/7/9 上午 10:01
@Author  : 银子
"""

import pytest
from PageObjects.login_page import LoginPage
from PageObjects.index_page import IndexPage
from TestDatas.login_datas.commonDatas import CommonDatas as cd
from TestDatas.login_datas.loginDatas import LoginDatas as ld

from Common import dir_config
from Common import logger
import logging

import time

@pytest.fixture()
def init(init_driver_cls):
    lp = LoginPage(init_driver_cls)
    ip = IndexPage(init_driver_cls)
    init_driver_cls.refresh()
    yield init_driver_cls,lp,ip


class Test_1_Login():

    # 异常用例--手机号码格式不正确（手机号为空、少于11位，多于11位，不在号码段）
    @pytest.mark.parametrize('data', ld.false_phtone)
    def test_0_login_phone_false(self,data,init):
        # 前置条件：打开登录页面,输入用户名、密码，点击登录
        init[1].login(data['phone'],data['passwd'])
        logging.info('------输入的手机号是{}，输入的密码是{}'.format(data['phone'],data['passwd']))
        # 获取页面错误信息
        # 断言，获取到页面错误提示信息与预期结果进行比对
        assert data['expectation'] == init[1].login_error_msg()

    # 异常用例--密码格式不正确（手机号为空、少于11位，多于11位，不在号码段）
    @pytest.mark.parametrize('data',ld.false_passwd)
    def test_1_login_passwd_false(self,data,init):
        # 输入用户名、密码，点击登录
        init[1].login(data['phone'], data['passwd'])
        # 获取页面错误信息,断言，获取到页面错误提示信息与预期结果进行比对
        assert data['expectation'] == init[1].page_content_error_msg()

    # 正常用例-登录成功
    @pytest.mark.parametrize('item', ld.true_data)
    def test_2_login_True(self,item,init):
        # 调用登录功能,传入测试数据，完成登录操作
        init[1].login(item['phone'],item['passwd'])
        # 断言 判断登录成功后是否有退出按钮
        try:
            assert init[2].index_exit()
            logging.info("断言成功，实际结果为{}".format(init[2].index_exit()))
        except:
            logging.exception("断言失败，错误信息为：")
            raise


class Test_2_Link():

    # 注册入口
    @pytest.mark.run
    def test_register_ent(self,init):
        # 点击注册链接
        init[1].click_register_enter()
        # 断言，获取到页面错误提示信息与预期结果进行比对

        assert "注册" == init[1].check_register_enter()


if __name__ == '__main__':

    # report_name = ('--html=' + dir_config.htmlreport_dir + 'report.html')
    # report_dir = "--html="+"\Outputs\HTML_reports\%sreport.html"\
    #             %time.strftime("%Y_%m_%d_%H_%M_%S")
    # print(report_dir)
    #pytest.main(['-s','-v'])
    pytest.main(['-s','-v', '-m','run','--html=Outputs\\HTML_reports\\reports.html'])