#比如说获取当前时间戳
#比如说强制等待
#比如说
import time
import unittest
from BeautifulReport import BeautifulReport
import datetime

def url():
    return "http://www.chandao.org"

def getZenDaoUrl():
    return "http://127.0.0.1"


def report():
    test_suite = unittest.defaultTestLoader.discover('../GxaTestCase', pattern='*case.py')

    result = BeautifulReport(test_suite)

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    result.report(filename=str(timestamp) + '测试报告', description='测试报告', report_dir='../report',
                  theme='theme_default')


def screen(a):
    timestamp = str(int(time.time()))
    a.get_screenshot_as_file('../截图/'+timestamp+".png")