
import unittest
import time

from BeautifulReport import BeautifulReport

import app

suite = unittest.TestLoader().discover(app.BASE_DIR + '/script', pattern='test*.py')
file_name = "test_BeautifulReport_{}.html".format(time.strftime("%Y%m%d%H%M%S"))
BeautifulReport(suite).report(filename=file_name,description="测试登录及添加员工模块用例报告", log_path=app.BASE_DIR + '/report')
print("*" * 30)
print("测试构建后的代码")
