import requests
from dbtools import query
from filetools import read_file
from filetools import write_file

#用户修改文章接口
# 1.构造请求
# nt = read_file("./user_token.txt")
# iid = read_file("./aiticle_id.txt")
u = "http://118.24.105.78:2333/article/update"              # 接口地址
# h = {"Content-Type":"application/json", "token":nt}            # 请求头
h = {"Content-Type":"application/json","token":"{}".format(read_file("./user_token.txt"))} 
d ={"title":"楞个干哈子嘛", "content":"风中", "tags":"测测测测测", "brief":"没得", "ximg":"dsfsdf.jpg", 
"aid":'{}'.format(read_file("./aiticle_id.txt")) }  # 请求参数
r = requests.post(url=u,headers=h,json=d)          # r 是返回值
print(r.text)                                      # r.text：响应值


# # 2.判断结果
# print( r.status_code)
assert r.status_code == 200       # 判断状态码， 获取本次响应的状态码是否等于200
# print(r.json())                   # r.json()：把返回值 r 转换成字典
assert r.json()["status"] == 200  # 判断结果码

# 3.数据库查询

# print(iid)
sql = "select * from t_article where id = '{}'".format(read_file("./aiticle_id.txt"))
assert len(query(sql)) !=0   # 如果账号存在 > sql应该是有结果的 > query(sql)长度 != 0
print("修改文章接口测试用例执行通过！")
print(query(sql))

