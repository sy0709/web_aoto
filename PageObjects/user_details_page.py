
from PageLocators.userDetailsPage_loc import UserDetailsLocators as loc
from Common.basepage import BasePage


class UserDetailsPage(BasePage):
    """实现个人中心页面功能"""

    # 获取个人帐户余额
    def get_user_money(self):
        # WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(loc.user_usable_momey))
        # return self.driver.find_element(*loc.user_usable_momey).text
        return self.get_element_text(loc.user_usable_momey,"个人资料页_获取个人账户余额").strip("元")

