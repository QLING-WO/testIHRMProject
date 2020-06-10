import logging
import unittest
from parameterized import parameterized

import app
from api.login_api import LoginApi
from utils import init_logging, assert_common, read_login_data

class TestIHRMLogin(unittest.TestCase):

    def setUp(self):
        self.logging = init_logging()
        self.login_api = LoginApi()

    def tearDown(self):
        pass

    # 定义登录数据文件的路径
    filepath = app.BASE_DIR + "/data/login_data.json"


    @parameterized.expand(read_login_data(filepath))
    def test01_login(self, case_name, request_body, success,code, message,http_code):
        # 使用封装的接口调用登录接口,并接受返回的响应数据
        response = self.login_api.login(request_body, {"Content-Type":"application/json"})
        logging.info("%s结果为:{}".format(response.json()) % case_name)

        assert_common(self, http_code, success, code, message, response)