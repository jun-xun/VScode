import requests
from dbtools import query
from filetools import read_file
from filetools import write_file

#用户登录
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

# 发表文章
# 1.构造请求
# nt = read_file("./user_token.txt")
u = "http://118.24.105.78:2333/article/new"              # 接口地址
# h = {"Content-Type":"application/json", "token":nt}           # 请求头
h = {"Content-Type":"application/json","token":"{}".format(read_file("./user_token.txt"))} 
d ={"title":"江月年年月相似", "content":"江畔何年初见月", "tags":"测试真的6", "brief":"江月何年初照人", "ximg":"dsfsdf.jpg"} # 请求参数
r = requests.post(url=u,headers=h,json=d)          # r 是返回值
print(r.text)

# 2.判断结果
# print(r.status_code)
assert r.status_code == 200       # 判断状态码
# print(r.json())
assert r.json()["status"] == 200  # 判断结果码

# 3.数据库查询
sql = "select * from t_article where title = '江月年年月相似'"
assert len(query(sql)) !=0   # 如果账号存在 > sql应该是有结果的 > query(sql)长度 != 0
print("发表文章接口测试用例执行通过！")
print(query(sql))

# 关联文章id
iid = r.json()["data"]["articleid"]
write_file("./aiticle_id.txt",str(iid)) 








