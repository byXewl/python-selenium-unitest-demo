"""

整个项目要公用的自动化方法
比如说元素定位。比如说打开网页

"""
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from GxaCommon.common import getZenDaoUrl, screen


class BasePage:

    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument('lang=zh_CN.UTF-8')
        options.add_argument('--start-maximized') #以最大窗口打开
        options.add_experimental_option('detach', True)
        options.add_experimental_option('useAutomationExtension', False)
        self.driver = webdriver.Chrome(options=options)

    def open_zentao(self):
        self.driver.get(getZenDaoUrl()+"/zentao/user-login.html")
        screen(self.driver)

    def login_zentao(self, username_xpath_value, password_xpath_value,username,password,login_button_xpath):
        self.find_username(username_xpath_value).send_keys(username)
        self.find_password(password_xpath_value).send_keys(password)
        self.find_login(login_button_xpath).click()
        sleep(2)
        screen(self.driver)
        return self.get_title()


    def logout_zentao(self):
        self.driver.execute_script("javascript:$.apps.logout()")
        sleep(2)
        screen(self.driver)
        return self.get_title()

    def get_title(self):
        return self.driver.title

    def get_current_url(self):
        return self.driver.current_url

    def open_url(self,url):
        self.driver.execute_script("window.open('"+url+"','_self')")
        sleep(2)
        return self.driver.title

    def find_ele(self, input_xpath_value):
        return self.driver.find_element(By.XPATH, input_xpath_value)

    def find_input(self, input_xpath_value):
        return self.driver.find_element(By.XPATH, input_xpath_value)

    def find_button(self, button_xpath_value):
        return self.driver.find_element(By.XPATH, button_xpath_value)

    # 保存成功的弹窗消息
    def save_alert(self,save_alert_xpath):
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, save_alert_xpath))
        )

    # 返回js弹出元素
    def find_alert(self):
        return self.driver.switch_to.alert

    # 同意js输入框
    def submit_alert(self):
        return self.driver.switch_to.alert.accept()

    def close_win(self):
        # self.driver.quit() 这个不要
        self.driver.close()

    def find_username(self, username_xpath_value):
        return self.driver.find_element(By.XPATH, username_xpath_value)

    def find_password(self, password_xpath_value):
        return self.driver.find_element(By.XPATH, password_xpath_value)

    def find_login(self, find_xpath_value):
        return self.driver.find_element(By.XPATH, find_xpath_value)