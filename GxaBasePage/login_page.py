'''
登录页面要使用到的最基础的操作
比如说定位账号
定位密码
定位登录
输入账号
输入密码
点击登录

继承basepage
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from GxaBasePage.basepage import BasePage


class LoginPage(BasePage):

    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument('lang=zh_CN.UTF-8')
        options.add_argument('--start-maximized')  # 以最大窗口打开
        options.add_experimental_option('detach', True)
        options.add_experimental_option('useAutomationExtension', False)
        self.driver = webdriver.Chrome(options=options)

    def find_username(self, username_xpath_value):
        return self.driver.find_element(By.XPATH, username_xpath_value)

    def find_password(self, password_xpath_value):
        return self.driver.find_element(By.XPATH, password_xpath_value)

    def find_login(self, find_xpath_value):
        return self.driver.find_element(By.XPATH, find_xpath_value)

    # 登录失败弹窗
    def find_login_fail_alert(self, fail_xpath_value):
        return WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, fail_xpath_value))
        )
