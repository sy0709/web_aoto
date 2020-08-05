import pytest
from selenium import webdriver
from TestDatas.login_datas.commonDatas import CommonDatas as cd
import logging

from PageObjects.login_page import LoginPage
from PageObjects.index_page import IndexPage


@pytest.fixture(scope='class')
def init_driver_cls():
    logging.info("开始执行用例---scope='class'整个测试类只执行一次")
    driver = webdriver.Chrome()
    driver.get(cd.login_url)
    driver.maximize_window()
    yield driver
    logging.info("执行完成清理工作---整个测试类只执行一次")
    driver.quit()


# 将打开浏览器，最大化网页，登录操作作为前置条件，关闭浏览器作为后置条件
@pytest.fixture()
def init_driver_fun():
    logging.info("开始执行用例---scope='function'每个测试执行一次")
    driver = webdriver.Chrome()
    driver.get(cd.login_url)
    driver.maximize_window()
    yield driver  # 需要返回浏览器对象
    logging.info("执行完成清理工作---每个测试类执行一次")
    driver.quit()


# 嵌套另一个fixture,获取驱动对象，然后刷新页面
@pytest.fixture()
def web_refresh(init_driver):
    init_driver.refresh()  # 刷新页面

