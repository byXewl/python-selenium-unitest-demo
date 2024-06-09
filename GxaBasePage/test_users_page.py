from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from GxaBasePage.basepage import BasePage
from GxaCommon.common import getZenDaoUrl, screen


class TestUsersPage(BasePage):

    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument('lang=zh_CN.UTF-8')
        options.add_argument('--start-maximized') #以最大窗口打开
        options.add_experimental_option('detach', True)
        options.add_experimental_option('useAutomationExtension', False)
        self.driver = webdriver.Chrome(options=options)

    def open_user_list(self):
        self.driver.get(getZenDaoUrl() + "/zentao/company-browse.html")
        # screen(self.driver)


    def find_username(self, username_xpath_value):
        return self.driver.find_element(By.XPATH, username_xpath_value)

    def find_password(self, password_xpath_value):
        return self.driver.find_element(By.XPATH, password_xpath_value)

    def find_admin_password(self,password_xpath_value):
        return self.driver.find_element(By.XPATH, password_xpath_value)

    def find_china_name(self, username_xpath_value):
        return self.driver.find_element(By.XPATH, username_xpath_value)
