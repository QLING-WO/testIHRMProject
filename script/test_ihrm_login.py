import logging

import requests
import unittest

from api.login_api import LoginApi
from utils import init_logging, assert_common


class TestIHRMLogin(unittest.TestCase):

    def setUp(self):
        self.logging = init_logging()
        self.login_api = LoginApi()

    def tearDown(self):
        pass

    # 编写登录成功函数
    def test01_login_success(self):
        # 使用封装的接口调用登录接口,并接受返回的响应数据
        response = self.login_api.login({"mobile":"13800000002","password":"123456"}, {"Content-Type":"application/json"})
        logging.info("登录成功的结果为:{}".format(response.json()))

        assert_common(self, 200, True, 10000, "操作成功", response)
        """
        self.assertEqual(200,response.status_code)
        self.assertEqual(True, response.json().get("success"))
        self.assertEqual(10000, response.json().get("code"))
        self.assertIn("操作成功", response.json().get("message"))
        """
    # 实现手机号码为空
    def test02_mobile_is_empty(self):
        # 使用封装的接口调用登录接口,并接受返回的响应数据
        response = self.login_api.login({"mobile": "", "password": "error"},
                                        {"Content-Type": "application/json"})
        logging.info("手机号码为空的结果为:{}".format(response.json()))

        assert_common(self, 200, False, 20001, "用户名或密码错误", response)

    def test03_mobile_is_not_exists(self):
        # 使用封装的接口调用登录接口,并接受返回的响应数据
        response = self.login_api.login({"mobile": "13802000702", "password": "123456"},
                                        {"Content-Type": "application/json"})
        logging.info("手机号码不存在的结果为:{}".format(response.json()))

        assert_common(self, 200, False, 20001, "用户名或密码错误", response)

    def test04_password_is_error(self):
        # 使用封装的接口调用登录接口,并接受返回的响应数据
        response = self.login_api.login({"mobile": "13800000002", "password": "1236"},
                                        {"Content-Type": "application/json"})
        logging.info("密码错误的结果为:{}".format(response.json()))

        assert_common(self, 200, False, 20001, "用户名或密码错误", response)

    def test05_params_is_none(self):
        # 使用封装的接口调用登录接口,并接受返回的响应数据
        response = self.login_api.login({},
                                        {"Content-Type": "application/json"})
        logging.info("无参的结果为:{}".format(response.json()))

        assert_common(self, 200, False, 20001, "用户名或密码错误", response)

    def test06_params_is_null(self):
        # 使用封装的接口调用登录接口,并接受返回的响应数据
        response = self.login_api.login(None,{"Content-Type": "application/json"})
        logging.info("传入None的结果为:{}".format(response.json()))

        assert_common(self, 200, False, 99999, "抱歉，系统繁忙，请稍后重试！", response)

    def test07_more_params(self):
        # 使用封装的接口调用登录接口,并接受返回的响应数据
        response = self.login_api.login({"mobile": "13800000002", "password": "123456","more_params":1},
                                        {"Content-Type": "application/json"})
        logging.info("多参的结果为:{}".format(response.json()))

        assert_common(self, 200, True, 10000, "操作成功", response)

    def test08_less_params_mobile(self):
        # 使用封装的接口调用登录接口,并接受返回的响应数据
        response = self.login_api.login({"password": "123456"},
                                        {"Content-Type": "application/json"})
        logging.info("缺少mobile参数的结果为:{}".format(response.json()))

        assert_common(self, 200, False, 20001, "用户名或密码错误", response)

    def test09_less_params_password(self):
        # 使用封装的接口调用登录接口,并接受返回的响应数据
        response = self.login_api.login({"mobile": "13800000002"},
                                        {"Content-Type": "application/json"})
        logging.info("缺少password参数的结果为:{}".format(response.json()))

        assert_common(self, 200, False, 20001, "用户名或密码错误", response)

    def test10_params_is_error(self):
        # 使用封装的接口调用登录接口,并接受返回的响应数据
        response = self.login_api.login({"moblie": "13800000002", "password": "123456"},
                                        {"Content-Type": "application/json"})
        logging.info("多参的结果为:{}".format(response.json()))

        assert_common(self, 200, False, 20001, "用户名或密码错误", response)

    def test11_password_is_empty(self):
        # 使用封装的接口调用登录接口,并接受返回的响应数据
        response = self.login_api.login({"mobile": "13800000002", "password": ""},
                                        {"Content-Type": "application/json"})
        logging.info("密码为空的结果为:{}".format(response.json()))

        assert_common(self, 200, False, 20001, "用户名或密码错误", response)