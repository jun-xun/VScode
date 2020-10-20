import requests
from dbtools import query
from filetools import read_file
from filetools import write_file

"""
# 使用get 方法去请求这个接口
# res = requests.get("http://118.24.105.78:2333/get_title_img")
# requests.get的意思是：我们使用get来请求 http://118.24.105.78:2333/get_title_img 这个接口
# 打印返回信息 
# print(res.text)
"""

# 1.构造请求
u = "http://118.24.105.78:2333/login"              # 接口地址
h = {"Content-Type":"application/json"}            # 请求头
d ={"username":"liuyun1", "password":"a12345678"}  # 请求参数
r = requests.post(url=u,headers=h,json=d)          # r 是返回值
print(r.text)                                      # r.text：响应值


# assert 条件语句，assert是python里用来断言的
# 2.判断结果
# print( r.status_code)
assert r.status_code == 200       # 判断状态码， 获取本次响应的状态码是否等于200
# print(r.json())                   # r.json()：把返回值 r 转换成字典
assert r.json()["status"] == 200  # 判断结果码

# 3.数据库查询
sql = "select * from t_user where username ='{}'".format(d["username"])
assert len(query(sql)) !=0   # 如果账号存在 > sql应该是有结果的 > query(sql)长度 != 0
print("登录接口测试用例执行通过！")

# 保存 token 到 user_name.txt 文件中
token = r.json()["data"]["token"]
write_file("./user_token.txt",token) # 把 token 写入 user_token.txt 文件中


# 用户退出
nt = read_file("./user_token.txt")
u = "http://118.24.105.78:2333/logout"              # 接口地址
h = {"Content-Type":"application/json","token":nt}            # 请求头
d ={"username":"liuyun1", "password":"a12345678"}  # 请求参数
r = requests.get(url=u,headers=h)          # r 是返回值
print(r.text)