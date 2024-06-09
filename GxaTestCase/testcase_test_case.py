'''
编写测试用例的测试用例
'''

"""
只存放登录的测试用例
"""

import time
import unittest

import ddt

from GxaProcess.test_testcase_process import TestTestCaseProcess


# TestCase代表测试用例类
@ddt.ddt
class Test_X(unittest.TestCase):

    def setUp(self):
        '''开始前的准备工作'''
        print("测试开始,登录进入禅道")
        self.zentaoProcess = TestTestCaseProcess()
        self.zentaoProcess.open_zentao()


    def tearDown(self):
        '''测试结束之后的工作'''
        print("测试结束")
        time.sleep(2)
        self.zentaoProcess.close_win()

    @ddt.file_data("login.json")
    @ddt.unpack
    def test_01(self,username,password):
        '''测试：禅道用例保存的测试，保存成功'''

        self.zentaoProcess.login_zentao("/html/body/div[1]/div/div[1]/div/div[2]/form/div[1]/input",
                                             "/html/body/div[1]/div/div[1]/div/div[2]/form/div[2]/input",
                                             username, password,
                                             "/html/body/div[1]/div/div[1]/div/div[2]/form/div[4]/button")

        a = self.zentaoProcess.add_testcase("/html/body/div[1]/div/div/div/div[2]/div/form/div[9]/div/input",
                                                     "第nn次创建用例",
                                                     "/html/body/div[1]/div/div/div/div[2]/div/form/div[15]/button")

        self.assertEqual(a, "第nn次创建用例")  # unittest 提供的断言方法
        print("测试成功:",a)

    @ddt.file_data("login.json")
    @ddt.unpack
    def test_02(self, username, password):
        '''测试：用例名称为空的保存,保存错误'''

        self.zentaoProcess.login_zentao("/html/body/div[1]/div/div[1]/div/div[2]/form/div[1]/input",
                                        "/html/body/div[1]/div/div[1]/div/div[2]/form/div[2]/input",
                                        username, password,
                                        "/html/body/div[1]/div/div[1]/div/div[2]/form/div[4]/button")

        b = self.zentaoProcess.add_testcase("/html/body/div[1]/div/div/div/div[2]/div/form/div[9]/div/input",
                                                    " ",
                                                     "/html/body/div[1]/div/div/div/div[2]/div/form/div[15]/button")
        self.assertEqual(b, "保存错误")  # unittest 提供的断言方法
        print("测试成功:",b)

    @ddt.file_data("login.json")
    @ddt.unpack
    def test_03(self, username, password):
        '''测试：登录禅道后，退出登录，再访问后台地址不可达'''

        self.zentaoProcess.login_zentao("/html/body/div[1]/div/div[1]/div/div[2]/form/div[1]/input",
                                        "/html/body/div[1]/div/div[1]/div/div[2]/form/div[2]/input",
                                        username, password,
                                        "/html/body/div[1]/div/div[1]/div/div[2]/form/div[4]/button")

        # 跳转登录返回title
        a = self.zentaoProcess.nologin_add_testcase()
        self.assertEqual(a, "用户登录 - 禅道")  # unittest 提供的断言方法
        print("测试成功:",a)

    @ddt.file_data("login.json")
    @ddt.unpack
    def test_04(self, username, password):
        '''测试：删除用例'''

        self.zentaoProcess.login_zentao("/html/body/div[1]/div/div[1]/div/div[2]/form/div[1]/input",
                                        "/html/body/div[1]/div/div[1]/div/div[2]/form/div[2]/input",
                                        username, password,
                                        "/html/body/div[1]/div/div[1]/div/div[2]/form/div[4]/button")

        a = self.zentaoProcess.del_testcase()
        self.assertEqual(a,"删除成功")
        print("测试成功:", a)


    @ddt.file_data("login.json")
    @ddt.unpack
    def test_05(self, username, password):
        '''测试：未登录删除用例，跳转重新登录'''

        self.zentaoProcess.login_zentao("/html/body/div[1]/div/div[1]/div/div[2]/form/div[1]/input",
                                        "/html/body/div[1]/div/div[1]/div/div[2]/form/div[2]/input",
                                        username, password,
                                        "/html/body/div[1]/div/div[1]/div/div[2]/form/div[4]/button")
        a = self.zentaoProcess.nologin_del_testcase()
        self.assertEqual(a, "用户登录 - 禅道")  # unittest 提供的断言方法
        print("测试成功:",a)

    @ddt.file_data("login.json")
    @ddt.unpack
    def test_06(self, username, password):
        '''测试：导出用例数据cvs'''

        self.zentaoProcess.login_zentao("/html/body/div[1]/div/div[1]/div/div[2]/form/div[1]/input",
                                        "/html/body/div[1]/div/div[1]/div/div[2]/form/div[2]/input",
                                        username, password,
                                        "/html/body/div[1]/div/div[1]/div/div[2]/form/div[4]/button")

        a = self.zentaoProcess.output_testcase()
        self.assertEqual(a, "导出成功")  # unittest 提供的断言方法
        print("测试成功:", a)

    @ddt.file_data("login.json")
    @ddt.unpack
    def test_07(self,username,password):
        '''测试：编辑已有测试用例，保存成功'''

        self.zentaoProcess.login_zentao("/html/body/div[1]/div/div[1]/div/div[2]/form/div[1]/input",
                                             "/html/body/div[1]/div/div[1]/div/div[2]/form/div[2]/input",
                                             username, password,
                                             "/html/body/div[1]/div/div[1]/div/div[2]/form/div[4]/button")

        a = self.zentaoProcess.edit_testcase("/html/body/div[1]/div/div/form/div[1]/div/div[1]/div[1]/div[1]/div[2]/div/input",
                                                     "编辑了创建的用例",
                                                     "/html/body/div[1]/div/div/form/div[2]/button[1]")

        self.assertEqual(a, "编辑了创建的用例")  # unittest 提供的断言方法
        print("测试成功:",a)

    @ddt.file_data("login.json")
    @ddt.unpack
    def test_08(self,username,password):
        '''测试：编辑已有测试用例，把用例名称为空保存'''

        self.zentaoProcess.login_zentao("/html/body/div[1]/div/div[1]/div/div[2]/form/div[1]/input",
                                             "/html/body/div[1]/div/div[1]/div/div[2]/form/div[2]/input",
                                             username, password,
                                             "/html/body/div[1]/div/div[1]/div/div[2]/form/div[4]/button")

        a = self.zentaoProcess.edit_testcase("/html/body/div[1]/div/div/form/div[1]/div/div[1]/div[1]/div[1]/div[2]/div/input",
                                                     " ",
                                                     "/html/body/div[1]/div/div/form/div[2]/button[1]")

        self.assertEqual(a, "保存错误")  # unittest 提供的断言方法
        print("测试成功:",a)

    @ddt.file_data("login.json")
    @ddt.unpack
    def test_09(self,username,password):
        '''测试：未登录访问编辑，跳转登录'''

        self.zentaoProcess.login_zentao("/html/body/div[1]/div/div[1]/div/div[2]/form/div[1]/input",
                                             "/html/body/div[1]/div/div[1]/div/div[2]/form/div[2]/input",
                                             username, password,
                                             "/html/body/div[1]/div/div[1]/div/div[2]/form/div[4]/button")

        a = self.zentaoProcess.nologin_edit_testcase("/html/body/div[1]/div/div/form/div[1]/div/div[1]/div[1]/div[1]/div[2]/div/input",
                                                     " ",
                                                     "/html/body/div[1]/div/div/form/div[2]/button[1]")

        self.assertEqual(a,"用户登录 - 禅道")  # unittest 提供的断言方法
        print("测试成功:",a)


if __name__ == '__main__':
    unittest.main()