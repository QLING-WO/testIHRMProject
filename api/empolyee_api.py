import requests


class EmployeeApi:

    def __init__(self):
        # 定义员工模块的url
        self.emp_url = "http://ihrm-test.itheima.net" + "/api/sys/user"

    def add_emp(self, username, mobile, headers):
        jsonData = {
            "username": username,
            "mobile": mobile,
            "timeOfEntry": "2020-05-05",
            "formOfEmployment": 1,
            "departmentName": "测试部",
            "departmentId": "1063678149528784896",
            "correctionTime": "2020-05-30T16:00:00.000Z"
        }
        # 发送添加员工接口并返回结果
        return requests.post(url=self.emp_url, json=jsonData, headers=headers)

    def query_emp(self, emp_id, headers):
        query_url = self.emp_url + "/" + emp_id
        return requests.get(url=query_url, headers=headers)

    def revise_emp(self, emp_id, headers, jsonData):
        revise_url = self.emp_url + "/" + emp_id
        return requests.put(url=revise_url, json=jsonData, headers=headers)

    def delete_emp(self, emp_id, headers):
        delete_url = self.emp_url + "/" + emp_id
        return requests.delete(url=delete_url, headers=headers)

