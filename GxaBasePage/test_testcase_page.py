"""
禅道编写测试用例页面：

比如说定位测试主题
定位测试步骤
定位提交

输入测试主题

输入测试步骤
点击提交、

继承basepage
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from GxaCommon.common import getZenDaoUrl, screen
from GxaBasePage.basepage import BasePage


class TestTestCasePage(BasePage):

    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument('lang=zh_CN.UTF-8')
        options.add_argument('--start-maximized') #以最大窗口打开
        options.add_experimental_option('detach', True)
        options.add_experimental_option('useAutomationExtension', False)
        self.driver = webdriver.Chrome(options=options)


    def open_zentao_add_case(self):
        self.driver.get(getZenDaoUrl()+"/zentao/testcase-create-1--0--0-0-from=global.html")
        # screen(self.driver)

    def open_zentao_list_case(self):
        self.driver.get(getZenDaoUrl() + "/zentao/testcase-browse-1-all.html")
        # screen(self.driver)
