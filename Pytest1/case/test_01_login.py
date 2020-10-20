import pytest
import requests

# 跨文件夹导入
import os, sys
sys.path.append(os.getcwd())

from utils.dbtools import query
from utils.filetools import write_file

# 测试用例
def test_01_login_success():
    # 1.构造请求
    u = "http://118.24.105.78:2333/login"
    h = {"Content-Type":"application/json"}
    d = {"username":"liuyun1", "password":"a12345678" }
    r = requests.post(url=u,headers=h,json=d)
    # 2.断言，判断结果
    assert r.status_code ==200
    assert r.json()["status"] ==200
    # 3.数据库验证
    sql = "select * from t_user where username = '{}'".format(d["username"])
    assert len(query(sql)) !=0
    print("登录接口测试用例通过！")

    # 保存 token
    token = r.json()["data"]["token"]
    write_file("./conf/user_token.txt",token)

def test_02_login_file_byerroneous_username():
     # 1.构造请求
    u = "http://118.24.105.78:2333/login"
    h = {"Content-Type":"application/json"}
    d = {"username":"liuyuiXXXp", "password":"a12345678" }
    r = requests.post(url=u,headers=h,json=d)
    # print(r.text)
    # 2.断言，判断结果
    assert r.status_code ==200
    assert r.json()["status"] == 401
    # 3.数据库验证
    sql = "select * from t_user where username = '{}'".format(d["username"])
    assert len(query(sql)) ==0
    
