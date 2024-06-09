"""
继承或者调用login_page
将里面的元素组合成登录的业务

比如说又成功登录的流程
有失败登陆的流程
"""

import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from GxaBasePage.login_page import LoginPage


class LoginProcess(LoginPage):

    def login_zentao(self, username_xpath_value, password_xpath_value,username,password,login_button_xpath):
        self.find_username(username_xpath_value).send_keys(username)
        self.find_password(password_xpath_value).send_keys(password)
        self.find_login(login_button_xpath).click()
        time.sleep(2)
        return self.get_title()

    def logout_zentao(self):
        self.driver.execute_script("javascript:$.apps.logout()")
        time.sleep(2)
        return self.get_title()


    def login_zentao_more(self,username_xpath_value, password_xpath_value,username,password,login_button_xpath):
        self.find_username(username_xpath_value).send_keys(username)
        self.find_password(password_xpath_value).send_keys(password)
        self.find_login(login_button_xpath).click()

        # 提示失败，点击确认失败，继续登录
        for i in range(7):
            self.find_login_fail_alert("/html/body/div[2]/div/div/div[3]/nav/button").click()
            self.find_login(login_button_xpath).click()
            time.sleep(0.5)

        return self.find_login_fail_alert("/html/body/div[2]/div/div/div[2]/div").text

    def nologin_zentao_admin(self, username_xpath_value, password_xpath_value,username,password,login_button_xpath):
        self.find_username(username_xpath_value).send_keys(username)
        self.find_password(password_xpath_value).send_keys(password)
        self.find_login(login_button_xpath).click()
        time.sleep(2)
        url = self.get_current_url()
        self.logout_zentao()
        return  self.open_url(url)