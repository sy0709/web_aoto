
from PageLocators.inverstPage_loc import IversPageLocators as loc

from Common.basepage import BasePage


class InverstPage(BasePage):
    """标详情页"""

    # 获取标可投金额
    def get_bid_money(self):
        return self.get_element_text(loc.bidable_amount,"标页面_获取标可投金额")

    # 获取用户余额
    def get_user_money(self):
        return self.get_element_attr(loc.Invest_input,'data-amount',"标页面_获取用户余额")

    # 输入金额2000,点击投标
    def user_invest(self,money):
        # 输入金额
        self.input_text(loc.Invest_input,money,"标页面_输入投资金额")
        self.click_element(loc.Invest_button,"标页面_点击“投标”按钮")

    # 投票成功弹窗-点击查看并激活
    def click_activa_button_in_success_popup(self):
        self.click_element(loc.activa_button_in_success_popup,"标页面_投票成功弹窗-点击查看并激活")





