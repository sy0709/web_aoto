import time
from datetime import datetime
import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.remote.webdriver import WebDriver
from Common.handle_logger import case_logger
from Common.constants import OUTPUTS_DIR
from Common.upload_file import upload


class BasePage:
    '''
    BasePage类，针对PageObjects类的二次封装
    '''

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def wait_element_to_be_visible(self, loc, img_doc, timeout=20, frequency=0.5):
        '''
        等待元素可见
        :param loc: 元素定位的XPATH元组表达式
        :param img_doc: 截图说明
        :param timeout: 等待的超时时间
        :param frequency: 轮询频率
        :return:
        '''
        try:
            case_logger.info("开始等待页面元素<{}>是否可见！".format(loc))
            start_time = time.time()
            WebDriverWait(self.driver, timeout, frequency).until(EC.visibility_of_element_located(loc))
        except Exception as e:
            case_logger.error("页面元素<{}>等待可见失败！".format(loc))
            self.save_screenshot(img_doc)
            raise e
        else:
            end_time = time.time()
            case_logger.info("页面元素<{}>等待可见，等待时间：{}秒".format(loc, round(end_time - start_time, 2)))

    def wait_element_to_be_click(self, loc, img_doc, timeout=20, frequency=0.5):
        '''
        等待元素可点击
        :param loc: 元素定位的XPATH元组表达式
        :param img_doc: 截图说明
        :param timeout: 等待的超时时间
        :param frequency: 轮询频率
        :return:
        '''
        try:
            case_logger.info("开始等待页面元素<{}>是否可点击！".format(loc))
            start_time = time.time()
            WebDriverWait(self.driver, timeout, frequency).until(EC.element_to_be_clickable(loc))
        except Exception as e:
            case_logger.error("页面元素<{}>等待可点击失败！".format(loc))
            self.save_screenshot(img_doc)
            raise e
        else:
            end_time = time.time()
            case_logger.info("页面元素<{}>等待可点击，等待时间：{}秒".format(loc, round(end_time - start_time, 2)))

    def wait_element_to_be_exist(self, loc, img_doc, timeout=20, frequency=0.5):
        '''
        等待元素存在
        :param loc: 元素定位的XPATH元组表达式
        :param img_doc: 截图说明
        :param timeout: 等待的超时时间
        :param frequency: 轮询频率
        :return:
        '''
        try:
            case_logger.info("开始等待页面元素<{}>是否存在！".format(loc))
            start_time = time.time()
            WebDriverWait(self.driver, timeout, frequency).until(EC.presence_of_element_located(loc))
        except Exception as e:
            case_logger.error("页面元素<{}>等待存在失败！".format(loc))
            self.save_screenshot(img_doc)
            raise e
        else:
            end_time = time.time()
            case_logger.info("页面元素<{}>等待存在，等待时间：{}秒".format(loc, round(end_time - start_time, 2)))

    def save_screenshot(self, img_doc):
        '''
        页面截屏保存截图
        :param img_doc: 截图说明
        :return:
        '''
        file_name = OUTPUTS_DIR + "\\{}_{}.png".format(datetime.strftime(datetime.now(), "%Y%m%d%H%M%S"), img_doc)
        self.driver.save_screenshot(file_name)
        with open(file_name, mode='rb') as f:
            file = f.read()
        allure.attach(file, img_doc, allure.attachment_type.PNG)
        case_logger.info("页面截图文件保存在：{}".format(file_name))

    def get_element(self, loc, img_doc):
        '''
        获取页面中的元素
        :param loc: 元素定位的XPATH元组表达式
        :param img_doc: 截图说明
        :return: WebElement对象
        '''
        case_logger.info("在{}中查找元素<{}>".format(img_doc, loc))
        try:
            ele = self.driver.find_element(*loc)
        except Exception as e:
            case_logger.error("在{}中查找元素<{}>失败！".format(img_doc, loc))
            self.save_screenshot(img_doc)
            raise e
        else:
            return ele

    def get_elements(self, loc, img_doc):
        '''
        获取页面中的所有元素
        :param loc: 元素定位的XPATH元组表达式
        :param img_doc: 截图说明
        :return: WebElement对象
        '''
        case_logger.info("在{}中查找所有元素<{}>".format(img_doc, loc))
        try:
            ele = self.driver.find_elements(*loc)
        except Exception as e:
            case_logger.error("在{}中查找所有元素<{}>失败！".format(img_doc, loc))
            self.save_screenshot(img_doc)
            raise e
        else:
            return ele

    def input_text(self, text, loc, img_doc, timeout=20, frequency=0.5):
        '''
        对输入框输入文本内容
        :param text: 输入的文本内容
        :param loc: 元素定位的XPATH元组表达式
        :param img_doc: 截图说明
        :param timeout: 等待的超时时间
        :param frequency: 轮询频率
        :return:
        '''
        try:
            case_logger.info("在{}中输入元素<{}>的内容为{}".format(img_doc, loc, text))
            self.wait_element_to_be_visible(loc, img_doc, timeout, frequency)
            self.get_element(loc, img_doc).send_keys(text)
        except Exception as e:
            case_logger.error("在元素<{}>中输入内容{}失败！".format(loc, text))
            self.save_screenshot(img_doc)
            raise e

    def clear_text(self, loc, img_doc, timeout=20, frequency=0.5):
        '''
        清除文本框的内容
        :param loc: 元素定位的XPATH元组表达式
        :param img_doc: 截图说明
        :param timeout: 等待的超时时间
        :param frequency: 轮询频率
        :return:
        '''
        try:
            case_logger.info("在{}中清除元素<{}>的文本内容".format(img_doc, loc))
            self.wait_element_to_be_click(loc, img_doc, timeout, frequency)
            self.get_element(loc, img_doc).clear()
        except Exception as e:
            case_logger.error("在{}中清除元素<{}>的文本内容失败！".format(img_doc, loc))
            self.save_screenshot(img_doc)
            raise e

    def click_button(self, loc, img_doc, timeout=20, frequency=0.5):
        '''
        点击按钮
        :param loc: 元素定位的XPATH元组表达式
        :param img_doc: 截图说明
        :param timeout: 等待的超时时间
        :param frequency: 轮询频率
        :return:
        '''
        try:
            case_logger.info("在{}中点击元素<{}>".format(img_doc, loc))
            self.wait_element_to_be_click(loc, img_doc, timeout, frequency)
            self.get_element(loc, img_doc).click()
        except Exception as e:
            case_logger.error("在{}中点击元素<{}>失败！".format(img_doc, loc))
            self.save_screenshot(img_doc)
            raise e

    def get_element_text(self, loc, img_doc, timeout=20, frequency=0.5):
        '''
        获取WebElement对象的文本值
        :param loc: 元素定位的XPATH元组表达式
        :param img_doc: 截图说明
        :param timeout: 等待的超时时间
        :param frequency: 轮询频率
        :return: WebElement对象的文本值
        '''
        try:
            case_logger.info("在{}中获取元素<{}>的文本值".format(img_doc, loc))
            self.wait_element_to_be_visible(loc, img_doc, timeout, frequency)
            text = self.get_element(loc, img_doc).text
        except Exception as e:
            case_logger.error("在{}中获取元素<{}>的文本值失败！".format(img_doc, loc))
            self.save_screenshot(img_doc)
            raise e
        else:
            case_logger.info("获取到的元素文本值为：{}".format(text))
            return text

    def get_elements_text(self, loc, img_doc, timeout=20, frequency=0.5):
        '''
        获取WebElement对象的所有文本值
        :param loc: 元素定位的XPATH元组表达式
        :param img_doc: 截图说明
        :param timeout: 等待的超时时间
        :param frequency: 轮询频率
        :return: WebElement对象的文本值的列表
        '''
        try:
            case_logger.info("在{}中获取元素<{}>的所有文本值".format(img_doc, loc))
            self.wait_element_to_be_visible(loc, img_doc, timeout, frequency)
            all_text = self.get_elements(loc, img_doc)
            text_list = []
            for one_text in all_text:
                text_list.append(one_text.text)
        except Exception as e:
            case_logger.error("在{}中获取元素<{}>的所有文本值失败！".format(img_doc, loc))
            self.save_screenshot(img_doc)
            raise e
        else:
            case_logger.info("获取到的元素文本值列表为：{}".format(text_list))
            return text_list

    def get_element_attr(self, attr_name, loc, img_doc, timeout=20, frequency=0.5):
        '''
        获取WebElement对象的属性值
        :param attr_name: 属性名称
        :param loc: 元素定位的XPATH元组表达式
        :param img_doc: 截图说明
        :param timeout: 等待的超时时间
        :param frequency: 轮询频率
        :return: WebElement对象的属性值
        '''
        try:
            case_logger.info("在{}中获取元素<{}>的属性{}的值".format(img_doc, loc, attr_name))
            self.wait_element_to_be_exist(loc, img_doc, timeout, frequency)
            value = self.get_element(loc, img_doc).get_attribute(attr_name)
        except Exception as e:
            case_logger.error("在{}中获取元素<{}>的属性{}的值失败！".format(img_doc, loc, attr_name))
            self.save_screenshot(img_doc)
            raise e
        else:
            case_logger.info("获取到的元素属性{}的值为{}".format(attr_name, value))
            return value

    def switch_to_frame(self, loc, img_doc, timeout=20, frequency=0.5):
        '''
        切换iframe页面
        :param loc: 元素定位的XPATH元组表达式
        :param img_doc: 截图说明
        :param timeout: 等待的超时时间
        :param frequency: 轮询频率
        :return:
        '''
        try:
            case_logger.info("在{}中根据元素<{}>进行iframe切换".format(img_doc, loc))
            start_time = time.time()
            WebDriverWait(self.driver, timeout, frequency).until(EC.frame_to_be_available_and_switch_to_it(loc))
        except Exception as e:
            case_logger.error("在{}中根据元素<{}>进行iframe切换失败！".format(img_doc, loc))
            self.save_screenshot(img_doc)
            raise e
        else:
            end_time = time.time()
            case_logger.info("在{}中根据元素<{}>进行iframe切换，等待时间：{}秒".
                             format(img_doc, loc, round(end_time - start_time, 2)))

    def switch_to_default_content(self, img_doc):
        '''
        切换iframe到main页面
        :param img_doc: 截图说明
        :return:
        '''
        try:
            case_logger.info("切换iframe到main页面")
            self.driver.switch_to.default_content()
        except Exception as e:
            case_logger.error("切换iframe到main页面失败！")
            self.save_screenshot(img_doc)
            raise e

    def switch_to_parent(self, img_doc):
        '''
        切换iframe到上一层页面
        :param img_doc: 截图说明
        :return:
        '''
        try:
            case_logger.info("切换iframe到上一层页面")
            self.driver.switch_to.parent_frame()
        except Exception as e:
            case_logger.error("切换iframe到上一层页面失败！")
            self.save_screenshot(img_doc)
            raise e

    def upload_file(self, filename, img_doc, browser_type="chrome"):
        '''
        非input标签的文件上传
        :param filename: 文件名（绝对路径）
        :param img_doc: 截图说明
        :param browser_type: 浏览器类型
        :return:
        '''
        try:
            case_logger.info("上传文件（{}）".format(filename))
            time.sleep(2)
            upload(filePath=filename, browser_type=browser_type)
        except Exception as e:
            case_logger.error("上传文件（{}）失败！".format(filename))
            self.save_screenshot(img_doc)
            raise e
        else:
            time.sleep(2)

    def suspend_mouse(self, loc, img_doc, timeout=20, frequency=0.5):
        '''
        鼠标悬浮
        :param loc: 元素定位的XPATH元组表达式
        :param img_doc: 截图说明
        :param timeout: 等待的超时时间
        :param frequency: 轮询频率
        :return:
        '''
        try:
            case_logger.info("在{}上根据元素<{}>进行悬浮".format(img_doc, loc))
            self.wait_element_to_be_click(loc, img_doc, timeout, frequency)
            ele = self.get_element(loc, img_doc)
            ActionChains(self.driver).move_to_element(ele).perform()
        except Exception as e:
            case_logger.error("在{}上根据元素<{}>进行悬浮失败！".format(img_doc, loc))
            self.save_screenshot(img_doc)
            raise e

    def alert_close(self, img_doc, alert_type='alert', text=None, timeout=20, frequency=0.5):
        '''
        弹框关闭
        :param img_doc: 截图说明
        :param alert_type: 弹框类型：alert/confirm/prompt
        :param text: prompt弹框输入的文本
        :param timeout: 等待的超时时间
        :param frequency: 轮询频率
        :return:
        '''
        try:
            case_logger.info("在{}中切换并关闭{}类型的弹框".format(img_doc, alert_type))
            start_time = time.time()
            WebDriverWait(self.driver, timeout, frequency).until(EC.alert_is_present())
            if alert_type in ['alert', 'confirm']:
                self.driver.switch_to.alert.accept()
            elif alert_type == 'prompt':
                self.driver.switch_to.alert.send_keys(text)
                self.driver.switch_to.alert.accept()
            else:
                case_logger.error("不支持{},请确认alert的类型".format(alert_type))
        except Exception as e:
            case_logger.error("在{}中切换并关闭{}类型的弹框失败！".format(img_doc, alert_type))
            self.save_screenshot(img_doc)
            raise e
        else:
            end_time = time.time()
            case_logger.info("在{}中切换并关闭{}类型的弹框，等待时间：{}秒".
                             format(img_doc, alert_type, round(end_time - start_time, 2)))

    def select_action(self, loc, img_doc, content, select_type, timeout=20, frequency=0.5):
        '''
        Select操作
        :param loc: 元素定位的XPATH元组表达式
        :param img_doc: 截图说明
        :param content: select_by_方法的入参
        :param select_type: select类型
        :param timeout: 等待的超时时间
        :param frequency: 轮询频率
        :return:
        '''
        try:
            case_logger.info("在{}上根据元素<{}>以{}方式进行下拉选择".format(img_doc, loc, select_type))
            self.wait_element_to_be_click(loc, img_doc, timeout, frequency)
            ele = self.get_element(loc, img_doc)
            if select_type == 'index':
                Select(ele).select_by_index(content)
            elif select_type == 'value':
                Select(ele).select_by_value(content)
            elif select_type == 'text':
                Select(ele).select_by_visible_text(content)
            else:
                case_logger.error("不支持{},请确认Select的类型".format(select_type))
        except Exception as e:
            case_logger.error("在{}上根据元素<{}>以{}方式进行下拉选择失败！".format(img_doc, loc, select_type))
            self.save_screenshot(img_doc)
            raise e

    def switch_to_windows(self, loc, img_doc, timeout=20, frequency=0.5):
        '''
        窗口切换
        :param loc: 元素定位的XPATH元组表达式
        :param img_doc: 截图说明
        :param timeout: 等待的超时时间
        :param frequency: 轮询频率
        :return:
        '''
        try:
            case_logger.info("在{}中根据元素<{}>进行窗口切换".format(img_doc, loc))
            cur_handles = self.driver.window_handles  # 获取点击之前的窗口总数
            start_time = time.time()
            self.click_button(loc, img_doc, timeout, frequency)  # 点击按钮后新的窗口出现
            WebDriverWait(self.driver, timeout, frequency).until(EC.new_window_is_opened(cur_handles))
            wins = self.driver.window_handles  # 再次获取窗口总数
            self.driver.switch_to.window(wins[-1])  # 切换到新的页面
        except Exception as e:
            case_logger.error("在{}中根据元素<{}>进行窗口切换失败！".format(img_doc, loc))
            self.save_screenshot(img_doc)
            raise e
        else:
            end_time = time.time()
            case_logger.info("在{}中根据元素<{}>进行窗口切换，等待时间：{}秒".
                             format(img_doc, loc, round(end_time - start_time, 2)))