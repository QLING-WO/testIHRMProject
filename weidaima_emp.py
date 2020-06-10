import requests

# 发送登录接口请求
response = requests.post(url="http://ihrm-test.itheima.net/api/sys/login", json={"mobile":"13800000002","password":"123456"}, headers={"Content-Type":"application/json"})

print("登录结果为:", response.json())

# 提取登录返回的令牌
token = 'Bearer '+response.json().get('data')
print("提取到的令牌是:",token)

# 发送添加员工接口
headers = {"Content-Type":"application/json","Authorization":token}
response = requests.post(url="http://ihrm-test.itheima.net" + "/api/sys/user",
                         json={
                             "username": "尼古户皮卡皮皮",
                             "mobile": "1578840028",
                             "timeOfEntry": "2020-05-05",
                             "formOfEmployment": 1,
                             "departmentName": "测试部",
                             "departmentId": "1063678149528784896",
                             "correctionTime": "2020-05-30T16:00:00.000Z"
                         },
                         headers=headers
                         )
# 打印添加员工的接口
print("添加员工的接口返回数据为:", response.json())
# 提取添加员工接口返回的员工id
emp_id = response.json().get('data').get('id')
print("提取员工的id为:", emp_id)


# 拼接查询员工接口的URL
query_url = "http://ihrm-test.itheima.net" + "/api/sys/user" +"/" +emp_id
print("拼接查询员工接口的url为:", query_url)
# 发送查询员工接口的请求
response = requests.get(url=query_url, headers=headers)
# 打印查询员工的结果
print("打印查询员工的结果为:",response.json())

# 拼接修改员工的URL
modify_url = "http://ihrm-test.itheima.net" + "/api/sys/user"  +"/" +emp_id
# 发送修改员工的接口请求
response = requests.put(url=modify_url,json={"username": "尼古户皮卡皮皮"}, headers=headers)
# 打印修改员工的结果
print("打印修改员工的结果为:",response.json())

# 拼接删除员工的URL
delete_url = "http://ihrm-test.itheima.net" + "/api/sys/user"  +"/" +emp_id
# 发送删除员工的接口请求
response = requests.delete(url=delete_url, headers=headers)
# 打印删除员工的结果
print("打印删除员工的结果为:",response.json())