import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from GxaBasePage.test_users_page import TestUsersPage


class TestUsersProcess(TestUsersPage):

    def add_user(self, china_name_xpath_value, username_xpath_value, password_xpath_value, two_password_xpath_value,admin_password_xpath_value,
                 china_name, username, password,two_password, admin_password, add_button_xpath):
        self.open_user_list()

        # 进入frame
        WebDriverWait(self.driver, 10).until(
            EC.frame_to_be_available_and_switch_to_it((By.ID, "appIframe-admin"))
        )
        time.sleep(2)

        # 点击添加用户的<a>
        self.find_ele("/html/body/div[1]/div/div[1]/div[2]/div/a").click()
        time.sleep(2)

        self.find_ele(china_name_xpath_value).send_keys(china_name)
        self.find_username(username_xpath_value).send_keys(username)
        self.find_password(password_xpath_value).send_keys(password)
        self.find_password(two_password_xpath_value).send_keys(two_password)
        self.find_ele(admin_password_xpath_value).send_keys(admin_password)
        self.find_ele(add_button_xpath).click()

        time.sleep(2)

        return self.get_title()