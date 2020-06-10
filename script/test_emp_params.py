import logging
import unittest

from parameterized import parameterized

import app
from api.empolyee_api import EmployeeApi
from api.login_api import LoginApi
from utils import assert_common, read_emp_data


class TestIHRMEmployee(unittest.TestCase):

    def setUp(self):
        self.login_api = LoginApi()
        self.emp_api = EmployeeApi()

    def tearDown(self):
        pass

    def test01_login_success(self):
        # 发送登录的接口请求
        jsonData = {"mobile": "13800000002", "password": "123456"}
        response = self.login_api.login(jsonData, {"Content-Type": "application/json"})
        # 打印登录接口
        logging.info("登录结果为:{}".format(response.json()))
        # 提取登录返回的令牌
        token = 'Bearer ' + response.json().get('data')
        # 把令牌拼接成HEADERS并保存到全局变量
        app.HEADERS = {"Content-Type": "application/json", "Authorization": token}
        logging.info("保存到全局变量中的请求头为:{}".format(app.HEADERS))

    emp_path = app.BASE_DIR + "/data/emp_data.json"


    @parameterized.expand(read_emp_data(emp_path, 'add_emp'))
    def test02_add_emp_success(self, username, mobile, success, code, message, http_code):
        # 发送添加员工的接口请求
        response = self.emp_api.add_emp(username, mobile, app.HEADERS)
        logging.info("添加员工得结果为:{}".format(response.json()))
        app.EMP_ID = response.json().get('data').get('id')
        logging.info("保存到全局变量的员工ID为:{}".format(app.EMP_ID))
        assert_common(self, http_code, success, code, message, response)

    @parameterized.expand(read_emp_data(emp_path, "query_emp"))
    def test03_query_emp_success(self, success, code, message, http_code):
        response = self.emp_api.query_emp(app.EMP_ID, app.HEADERS)
        logging.info("查询员工得信息为:{}".format(response.json()))
        assert_common(self, http_code, success, code, message, response)

    @parameterized.expand(read_emp_data(emp_path, "modify_emp"))
    def test04_modify_emp_success(self, username, success, code, message, http_code):
        data = {"username": username}
        response = self.emp_api.revise_emp(app.EMP_ID, app.HEADERS, data)
        logging.info("修改员工得信息为:{}".format(response.json()))
        assert_common(self, http_code, success, code, message, response)

    @parameterized.expand(read_emp_data(emp_path, "delete_emp"))
    def test05_delete_emp_success(self, success, code, message, http_code):
        response = self.emp_api.delete_emp(app.EMP_ID, app.HEADERS)
        logging.info("删除员工得信息为:{}".format(response.json()))
        assert_common(self, http_code, success, code, message, response)
