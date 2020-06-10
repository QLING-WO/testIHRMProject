import json
from logging import handlers
import  app
import logging

# 编写初始化日志的代码
# 首先定义一个初始化日志的函数
def init_logging():
# 在函数中设置日志器
    logger = logging.getLogger()
# 设置日志等级
    logger.setLevel(logging.INFO)
# 设置控制台处理器
    sh = logging.StreamHandler()
# 设置文件处理器
    log_path = app.BASE_DIR + "/log/ihrm.log"
    fh = logging.handlers.TimedRotatingFileHandler(filename=log_path, when='M', interval=1, backupCount=3, encoding="utf-8")
# 设置格式化器
    fmt = '%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s'
    formatter = logging.Formatter(fmt)
# 将格式化器添加到文件处理器和控制台处理当中
    sh.setFormatter(formatter)
    fh.setFormatter(formatter)
# 将文件处理器和控制台处理器添加到日志器中
    logger.addHandler(sh)
    logger.addHandler(fh)


def assert_common(self, http_code, success, code, message, response):
    self.assertEqual(http_code, response.status_code)
    self.assertEqual(success, response.json().get("success"))
    self.assertEqual(code, response.json().get("code"))
    self.assertIn(message, response.json().get("message"))


# 编写读取登录数据的函数
def read_login_data(filepath):
    result_list =[]
    with open(filepath, mode="r", encoding="utf-8") as t:
        # 使用json加载数据文件为json格式
        jsonData = json.load(t)
        # 遍历json格式的数据文件,并把数据处理成列表元祖形式
        for login_data in jsonData: #type:dict
            result_list.append(tuple(login_data.values()))
    print("查看读取的登录数据:", result_list)
    return result_list

# 编写读取员工模块的数据函数
def read_emp_data(filepath, interface_name):
    # 打开数据文件
    with open(filepath, mode='r', encoding='utf-8') as f:
    # 把数据问价加载成json格式
        jsonData = json.load(f)
    # 读取加载的json数据当中,对用接口的数据
        emp_data = jsonData.get(interface_name) #type:dict

    # 把数据处理成列表元祖对象,然后添加到空列表中
        result_list = []
        result_list.append(tuple(emp_data.values()))
    print("读取的{}员工数据为:{}".format(interface_name,emp_data))

    # 返回数据
    return result_list


if __name__ == '__main__':
    filepath = app.BASE_DIR + "/data/login_data.json"
    result = read_login_data(filepath)
    # filepath = app.BASE_DIR + "/data/emp_data.json"
    # result = read_emp_data(filepath, "add_emp")
    # result = read_emp_data(filepath, "query_emp")
    # result = read_emp_data(filepath, "modify_emp")
    # result = read_emp_data(filepath, "delete_emp")
