# 实现员工管理模块的登录
import requests

# 发送登录接口请求
response = requests.post(url="http://ihrm-test.itheima.net/api/sys/login", json={"mobile":"13800000002","password":"123456"}, headers={"Content-Type":"application/json"})

print("登录结果为:", response.json())