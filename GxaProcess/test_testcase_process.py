"""
禅道这个项目编写测试用例的流程

 比如说
 封装一个方法test_testcase:
 包括登录的步骤
 点击测试
 打开测试用例
 输入测试主题
 输入步骤
 输入测试预期结果
 点击提交
"""
import re
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from GxaBasePage.test_testcase_page import TestTestCasePage


class TestTestCaseProcess(TestTestCasePage):

    def add_testcase(self, case_name_xpath, case_name, save_button_xpath):

        # 打开添加页
        self.open_zentao_add_case()

        # 进入frame
        WebDriverWait(self.driver, 10).until(
            EC.frame_to_be_available_and_switch_to_it((By.ID, "appIframe-qa"))
        )
        time.sleep(2)
        self.find_username(case_name_xpath).send_keys(case_name)
        self.find_button(save_button_xpath).click()

        time.sleep(2)

        try:
            caseName = self.find_ele(
                "/html/body/div[1]/div/div[2]/div[2]/div[1]/div/div/div[2]/div[1]/div/div[2]/div/a").text
        except Exception as e:  # 捕获所有异常
            return "保存错误"

        return caseName

    def nologin_add_testcase(self):
        # 退出未登录
        self.logout_zentao()

        # 打开添加页
        self.open_zentao_add_case()

        time.sleep(2)

        return self.get_title()

    def del_testcase(self):
        self.open_zentao_list_case()



        # 进入frame
        WebDriverWait(self.driver, 10).until(
            EC.frame_to_be_available_and_switch_to_it((By.ID, "appIframe-qa"))
        )
        time.sleep(3)

        a = self.find_ele(
            "/html/body/div[1]/div/div[2]/div[2]/div[1]/div/div/div[2]/div[1]/div/div[2]/div/a")
        url1 = a.get_attribute('href')
        del_url = re.sub(r'(view)', 'delete', url1)
        # print(del_url)

        # 删除
        self.driver.execute_script("window.open('"+del_url+"','_self')")
        self.submit_alert()


        '''
        self.find_ele(
            "/html/body/div[1]/div/div[2]/div[2]/div[1]/div/div/div[2]/div[1]/div/div[2]/div/a").click()

        time.sleep(2)
        self.find_ele(
            "/html/body/div[1]/div/div/div/div[2]/div[1]/div[3]/div/div/a[6]").click()

        self.driver.switch_to.default_content()
        WebDriverWait(self.driver, 10).until(
            EC.frame_to_be_available_and_switch_to_it((By.ID, "appIframe-qa"))
        )

        alert_button = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/div[5]/div/div/div[3]/nav/button[1]"))
        )
        alert_button.click()
        '''


        time.sleep(3)
        a = self.find_ele(
            "/html/body/div[1]/div/div[2]/div[2]/div[1]/div/div/div[2]/div[1]/div/div[2]/div/a")
        url2 = a.get_attribute('href')


        if url1 != url2 :
            return  "删除成功"
        else:
            return  "删除失败"

    def nologin_del_testcase(self):
        self.open_zentao_list_case()

        # 进入frame
        WebDriverWait(self.driver, 10).until(
            EC.frame_to_be_available_and_switch_to_it((By.ID, "appIframe-qa"))
        )
        time.sleep(3)

        a = self.find_ele(
            "/html/body/div[1]/div/div[2]/div[2]/div[1]/div/div/div[2]/div[1]/div/div[2]/div/a")
        url1 = a.get_attribute('href')
        del_url = re.sub(r'(view)', 'delete', url1)
        # print(del_url)


        # 退出未登录
        self.logout_zentao()

        # 删除
        self.driver.execute_script("window.open('" + del_url + "','_self')")

        time.sleep(2)

        return self.get_title()

    def output_testcase(self):
        self.open_zentao_list_case()

        # 进入frame
        WebDriverWait(self.driver, 10).until(
            EC.frame_to_be_available_and_switch_to_it((By.ID, "appIframe-qa"))
        )
        time.sleep(3)

        try:

            self.find_ele(
                "/html/body/div[1]/div/div[1]/div[2]/button[2]").click()

            self.find_ele(
                "/html/body/div[2]/menu/menu/li[1]/a/div/div").click()

            button = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/div[3]/div/div/form/div[8]/div/button"))
            )
            button.click()

            time.sleep(8)

        except Exception as e:  # 捕获所有异常
            return "导出错误"

        return "导出成功"

    def edit_testcase(self, case_name_xpath, case_name, save_button_xpath):
        self.open_zentao_list_case()


        # 进入frame
        WebDriverWait(self.driver, 15).until(
            EC.frame_to_be_available_and_switch_to_it((By.ID, "appIframe-qa"))
        )
        time.sleep(3)

        self.find_ele(
            "/html/body/div[1]/div/div[2]/div[2]/div[1]/div/div/div[2]/div[3]/div/div[1]/div/nav/a[3]").click()

        time.sleep(3)
        self.find_button(case_name_xpath).clear()
        self.find_username(case_name_xpath).send_keys(case_name)
        self.find_button(save_button_xpath).click()

        self.open_zentao_list_case()

        # 进入frame
        WebDriverWait(self.driver, 10).until(
            EC.frame_to_be_available_and_switch_to_it((By.ID, "appIframe-qa"))
        )
        time.sleep(3)

        try:
            caseName = self.find_ele(
                "/html/body/div[1]/div/div[2]/div[2]/div[1]/div/div/div[2]/div[1]/div/div[2]/div/a").text
            if caseName != case_name:
                return "保存错误"
        except Exception as e:  # 捕获所有异常
            return "保存错误"

        return caseName

    def nologin_edit_testcase(self, case_name_xpath, case_name, save_button_xpath):
        self.open_zentao_list_case()

        # 进入frame
        WebDriverWait(self.driver, 10).until(
            EC.frame_to_be_available_and_switch_to_it((By.ID, "appIframe-qa"))
        )
        time.sleep(3)

        a = self.find_ele(
            "/html/body/div[1]/div/div[2]/div[2]/div[1]/div/div/div[2]/div[3]/div/div[1]/div/nav/a[3]")
        url1 = a.get_attribute('href')

        # 退出未登录
        self.logout_zentao()

        # 访问
        self.driver.execute_script("window.open('"+url1+"','_self')")

        time.sleep(2)

        return self.get_title()
