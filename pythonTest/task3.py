import requests
from filetools import read_file

# 用户退出
# 1.构造请求
# nt = read_file("./user_token.txt")
u = "http://118.24.105.78:2333/logout"              # 接口地址
h = {"Content-Type":"application/json","token":"{}".format(read_file("./user_token.txt"))}            # 请求头
  # 请求参数
r = requests.get(url=u,headers=h)          # r 是返回值
print(r.text)                                      # r.text：响应值

#2.判断结果
# print( r.status_code)
assert r.status_code == 200       # 判断状态码， 获取本次响应的状态码是否等于200
# print(r.json())                   # r.json()：把返回值 r 转换成字典
assert r.json()["status"] == 200  # 判断结果码

print("用户退出接口测试用例执行通过！")

