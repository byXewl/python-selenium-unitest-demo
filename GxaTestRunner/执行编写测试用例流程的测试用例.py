import unittest

from GxaTestCase.testcase_test_case import Test_X

# unittest.TestLoader.discover("",)
suite = unittest.TestSuite()
suite.addTest(Test_X("test_07_1_case1"))
# suite.addTest(Test_X("test_02"))

runner = unittest.TextTestRunner()
runner.run(suite)