'''
编写测试用例的测试用例
'''

"""
只存放登录的测试用例
"""

import time
import unittest

import ddt

from GxaProcess.test_users_process import TestUsersProcess


# TestCase代表测试用例类
@ddt.ddt
class Test_X(unittest.TestCase):

    def setUp(self):
        '''开始前的准备工作'''
        print("测试开始,登录进入禅道")
        self.zentaoProcess = TestUsersProcess()
        self.zentaoProcess.open_zentao()

    def tearDown(self):
        '''测试结束之后的工作'''
        print("测试结束")
        time.sleep(2)
        self.zentaoProcess.close_win()

    @ddt.file_data("login.json")
    @ddt.unpack
    def test_01(self, username, password):
        '''测试：添加用户，保存成功'''

        self.zentaoProcess.login_zentao("/html/body/div[1]/div/div[1]/div/div[2]/form/div[1]/input",
                                        "/html/body/div[1]/div/div[1]/div/div[2]/form/div[2]/input",
                                        username, password,
                                        "/html/body/div[1]/div/div[1]/div/div[2]/form/div[4]/button")
        timestamp = str(int(time.time()))
        a = self.zentaoProcess.add_user("/html/body/div[1]/div/div/div/div[2]/form/div[8]/div/input",
                                        "/html/body/div[1]/div/div/div/div[2]/form/div[4]/div/input",
                                        "/html/body/div[1]/div/div/div/div[2]/form/div[5]/div/div/input",
                                        "/html/body/div[1]/div/div/div/div[2]/form/div[6]/div/input",
                                        "/html/body/div[1]/div/div/div/div[2]/form/div[15]/div/input",
                                        "陈二狗",str("admin")+timestamp,"Chenjie100","Chenjie100",password,
                                        "/html/body/div[1]/div/div/div/div[2]/form/div[17]/div/button[1]"
                                        )

        self.assertEqual(a, "组织视图首页-部门 - 禅道")  # unittest 提供的断言方法
        print("测试成功:", a)

    @ddt.file_data("login.json")
    @ddt.unpack
    def test_02(self, username, password):
        '''测试：添加用户，空用户名，保存失败'''

        self.zentaoProcess.login_zentao("/html/body/div[1]/div/div[1]/div/div[2]/form/div[1]/input",
                                        "/html/body/div[1]/div/div[1]/div/div[2]/form/div[2]/input",
                                        username, password,
                                        "/html/body/div[1]/div/div[1]/div/div[2]/form/div[4]/button")
        timestamp = str(int(time.time()))
        a = self.zentaoProcess.add_user("/html/body/div[1]/div/div/div/div[2]/form/div[8]/div/input",
                                        "/html/body/div[1]/div/div/div/div[2]/form/div[4]/div/input",
                                        "/html/body/div[1]/div/div/div/div[2]/form/div[5]/div/div/input",
                                        "/html/body/div[1]/div/div/div/div[2]/form/div[6]/div/input",
                                        "/html/body/div[1]/div/div/div/div[2]/form/div[15]/div/input",
                                        "陈二狗"," ","Chenjie100","Chenjie100",password,
                                        "/html/body/div[1]/div/div/div/div[2]/form/div[17]/div/button[1]"
                                        )

        self.assertEqual(a, "添加用户 - 禅道")  # unittest 提供的断言方法
        print("测试成功:", a)

    @ddt.file_data("login.json")
    @ddt.unpack
    def test_03(self, username, password):
        '''测试：添加用户，两次密码不同，添加失败'''

        self.zentaoProcess.login_zentao("/html/body/div[1]/div/div[1]/div/div[2]/form/div[1]/input",
                                        "/html/body/div[1]/div/div[1]/div/div[2]/form/div[2]/input",
                                        username, password,
                                        "/html/body/div[1]/div/div[1]/div/div[2]/form/div[4]/button")
        timestamp = str(int(time.time()))
        a = self.zentaoProcess.add_user("/html/body/div[1]/div/div/div/div[2]/form/div[8]/div/input",
                                        "/html/body/div[1]/div/div/div/div[2]/form/div[4]/div/input",
                                        "/html/body/div[1]/div/div/div/div[2]/form/div[5]/div/div/input",
                                        "/html/body/div[1]/div/div/div/div[2]/form/div[6]/div/input",
                                        "/html/body/div[1]/div/div/div/div[2]/form/div[15]/div/input",
                                        "陈二狗", str("admin") + timestamp, "Chenjie100", "Chenjie101", password,
                                        "/html/body/div[1]/div/div/div/div[2]/form/div[17]/div/button[1]"
                                        )

        self.assertEqual(a, "添加用户 - 禅道")
        print("测试成功:", a)

    @ddt.file_data("login.json")
    @ddt.unpack
    def test_04(self, username, password):
        '''测试：添加用户，用户名已经存在，添加失败'''

        self.zentaoProcess.login_zentao("/html/body/div[1]/div/div[1]/div/div[2]/form/div[1]/input",
                                        "/html/body/div[1]/div/div[1]/div/div[2]/form/div[2]/input",
                                        username, password,
                                        "/html/body/div[1]/div/div[1]/div/div[2]/form/div[4]/button")
        timestamp = str(int(time.time()))
        a = self.zentaoProcess.add_user("/html/body/div[1]/div/div/div/div[2]/form/div[8]/div/input",
                                        "/html/body/div[1]/div/div/div/div[2]/form/div[4]/div/input",
                                        "/html/body/div[1]/div/div/div/div[2]/form/div[5]/div/div/input",
                                        "/html/body/div[1]/div/div/div/div[2]/form/div[6]/div/input",
                                        "/html/body/div[1]/div/div/div/div[2]/form/div[15]/div/input",
                                        "陈二狗", str("admin"), "Chenjie100", "Chenjie100", password,
                                        "/html/body/div[1]/div/div/div/div[2]/form/div[17]/div/button[1]"
                                        )

        self.assertEqual(a, "添加用户 - 禅道")
        print("测试成功:", a)

    @ddt.file_data("login.json")
    @ddt.unpack
    def test_05(self, username, password):
        '''测试：添加用户，管理员密码错误，添加失败'''

        self.zentaoProcess.login_zentao("/html/body/div[1]/div/div[1]/div/div[2]/form/div[1]/input",
                                        "/html/body/div[1]/div/div[1]/div/div[2]/form/div[2]/input",
                                        username, password,
                                        "/html/body/div[1]/div/div[1]/div/div[2]/form/div[4]/button")
        timestamp = str(int(time.time()))
        a = self.zentaoProcess.add_user("/html/body/div[1]/div/div/div/div[2]/form/div[8]/div/input",
                                        "/html/body/div[1]/div/div/div/div[2]/form/div[4]/div/input",
                                        "/html/body/div[1]/div/div/div/div[2]/form/div[5]/div/div/input",
                                        "/html/body/div[1]/div/div/div/div[2]/form/div[6]/div/input",
                                        "/html/body/div[1]/div/div/div/div[2]/form/div[15]/div/input",
                                        "陈二狗", str("admin")+timestamp, "Chenjie100", "Chenjie100", str(password)+"X_e",
                                        "/html/body/div[1]/div/div/div/div[2]/form/div[17]/div/button[1]"
                                        )

        self.assertEqual(a, "添加用户 - 禅道")
        print("测试成功:", a)



if __name__ == '__main__':
    unittest.main()
