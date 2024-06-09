"""
只存放登录的测试用例
"""

import time
import unittest

import ddt

from GxaProcess.login_process import LoginProcess


# TestCase代表测试用例类
@ddt.ddt
class Test_X(unittest.TestCase):
    def setUp(self):
        '''开始前的准备工作'''
        print("测试开始,登录进入禅道")
        self.zentaoProcess = LoginProcess()
        self.zentaoProcess.open_zentao()


    def tearDown(self):
        '''测试结束之后的工作'''
        print("测试结束")
        time.sleep(2)
        self.zentaoProcess.close_win()

    @ddt.file_data("login.json")
    @ddt.unpack
    def test_01(self,username,password):
        '''测试：登录禅道正确账号，正确密码'''

        # 登录成功返回title
        a = self.zentaoProcess.login_zentao("/html/body/div[1]/div/div[1]/div/div[2]/form/div[1]/input",
                                        "/html/body/div[1]/div/div[1]/div/div[2]/form/div[2]/input",
                                        str(username)+"2", password,
                                        "/html/body/div[1]/div/div[1]/div/div[2]/form/div[4]/button")

        self.assertEqual(a, "地盘 - 禅道")  # unittest 提供的断言方法
        print("测试成功:",a)

    @ddt.file_data("login.json")
    @ddt.unpack
    def test_02(self,username,password):
        '''测试：登录禅道正确账号，错误密码'''

        # 登录失败返回title
        a = self.zentaoProcess.login_zentao("/html/body/div[1]/div/div[1]/div/div[2]/form/div[1]/input",
                                        "/html/body/div[1]/div/div[1]/div/div[2]/form/div[2]/input",
                                        str(username)+"2", str(password)+"hh",
                                        "/html/body/div[1]/div/div[1]/div/div[2]/form/div[4]/button")

        self.assertEqual(a, "用户登录 - 禅道")  # unittest 提供的断言方法
        print("测试成功:",a)

    @ddt.file_data("login.json")
    @ddt.unpack
    def test_03(self,username,password):
        '''测试：登录禅道错误账号，正确密码'''

        # 登录失败返回title
        a = self.zentaoProcess.login_zentao("/html/body/div[1]/div/div[1]/div/div[2]/form/div[1]/input",
                                        "/html/body/div[1]/div/div[1]/div/div[2]/form/div[2]/input",
                                        str(username)+" by X_e", str(password),
                                        "/html/body/div[1]/div/div[1]/div/div[2]/form/div[4]/button")

        self.assertEqual(a, "用户登录 - 禅道")  # unittest 提供的断言方法
        print("测试成功:",a)

    @ddt.file_data("login.json")
    @ddt.unpack
    def test_04(self,username,password):
        '''测试：登录禅道错误账号，错误密码'''

        # 登录失败返回title
        a = self.zentaoProcess.login_zentao("/html/body/div[1]/div/div[1]/div/div[2]/form/div[1]/input",
                                        "/html/body/div[1]/div/div[1]/div/div[2]/form/div[2]/input",
                                        str(username)+"by X_e", str(password)+"X_e",
                                        "/html/body/div[1]/div/div[1]/div/div[2]/form/div[4]/button")

        self.assertEqual(a, "用户登录 - 禅道")  # unittest 提供的断言方法
        print("测试成功:",a)


    @ddt.file_data("login.json")
    @ddt.unpack
    def test_05(self,username,password):
        '''测试：登录账户多次错误，有提示'''

        # 返回弹窗消息内容
        a = self.zentaoProcess.login_zentao_more("/html/body/div[1]/div/div[1]/div/div[2]/form/div[1]/input",
                                        "/html/body/div[1]/div/div[1]/div/div[2]/form/div[2]/input",
                                        str(username)+"by X_e 1", str(password)+"X_e",
                                        "/html/body/div[1]/div/div[1]/div/div[2]/form/div[4]/button")


        self.assertEqual(a, "登录失败，请检查您的用户名或密码是否填写正确。")  # unittest 提供的断言方法
        print("测试成功:",a)

    @ddt.file_data("login.json")
    @ddt.unpack
    def test_06(self, username, password):
        '''测试：登录账号正确，密码多次错误，锁定'''

        # 返回弹窗消息内容
        a = self.zentaoProcess.login_zentao_more("/html/body/div[1]/div/div[1]/div/div[2]/form/div[1]/input",
                                                 "/html/body/div[1]/div/div[1]/div/div[2]/form/div[2]/input",
                                                 str(username) + "3", str(password) + "X_e",
                                                 "/html/body/div[1]/div/div[1]/div/div[2]/form/div[4]/button")

        self.assertEqual(a, "密码尝试次数太多，请联系管理员解锁，或10分钟后重试。")  # unittest 提供的断言方法
        print("测试成功:", a)

    @ddt.file_data("login.json")
    @ddt.unpack
    def test_07(self,username,password):
        '''测试：登录禅道后，退出登录成功'''


        self.zentaoProcess.login_zentao("/html/body/div[1]/div/div[1]/div/div[2]/form/div[1]/input",
                                        "/html/body/div[1]/div/div[1]/div/div[2]/form/div[2]/input",
                                        str(username)+"2", str(password),
                                        "/html/body/div[1]/div/div[1]/div/div[2]/form/div[4]/button")
        # 退出返回title
        a = self.zentaoProcess.logout_zentao()
        self.assertEqual(a, "用户登录 - 禅道")  # unittest 提供的断言方法
        print("测试成功:",a)




    @ddt.file_data("login.json")
    @ddt.unpack
    def test_08(self,username,password):
        '''测试：登录禅道后，退出登录，再访问后台地址不可达'''

        # 跳转登录返回title
        a = self.zentaoProcess.nologin_zentao_admin("/html/body/div[1]/div/div[1]/div/div[2]/form/div[1]/input",
                                        "/html/body/div[1]/div/div[1]/div/div[2]/form/div[2]/input",
                                        str(username)+"2", str(password),
                                        "/html/body/div[1]/div/div[1]/div/div[2]/form/div[4]/button")
        self.assertEqual(a, "用户登录 - 禅道")  # unittest 提供的断言方法
        print("测试成功:",a)


if __name__ == '__main__':
     unittest.main()

