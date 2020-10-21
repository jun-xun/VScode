import pytest
import requests

# 跨文件夹导入
import os, sys
sys.path.append(os.getcwd())

from utils.dbtools import query
from utils.commontools import get_url
from utils.filetools import write_file
from utils.exceltools import read_excel

data = read_excel(excel_path="data\测谈网接口测试用例.xlsx", sheet_name='登录')

# 测试用例
def test_01_login_success():
    # 1.构造请求
    # print(type(data[0][2]))
    # u = get_url("/login")
    # u = data[0][2]
    u = eval(data[0][2])  # 因为返回的 data 数据是字符串类型，这里的 eval 把字符串转换成对应的类型
    h = eval(data[0][3])  # eval 把字典类型的字符串转换成 字典
    d = eval(data[0][4])
    r = requests.post(url=u,headers=h,json=d)
    # 2.断言，判断结果
    assert r.status_code ==int(data[0][5])
    assert r.json()["status"] ==int(data[0][6])
    # 3.数据库验证
    sql = "select * from t_user where username = '{}'".format(d["username"])
    assert len(query(sql)) !=0
    print("登录接口测试用例通过！")

    # 保存 token
    token = r.json()["data"]["token"]
    write_file("./conf/user_token.txt",token)

def test_02_login_file_byerroneous_username():
     # 1.构造请求
    # u = "http://118.24.105.78:2333/login"
    # h = {"Content-Type":"application/json"}
    # d = {"username":"liuyuiXXXp", "password":"a12345678" }
    
    u = eval(data[1][2])  # 因为返回的 data 数据是字符串类型，这里的 eval 把字符串转换成对应的类型
    h = eval(data[1][3])  # eval 把字典类型的字符串转换成 字典
    d = eval(data[1][4])
    r = requests.post(url=u,headers=h,json=d)
    # print(r.text)
    # 2.断言，判断结果
    assert r.status_code ==int(data[1][5])
    assert r.json()["status"] ==int(data[1][6])
    # 3.数据库验证
    sql = "select * from t_user where username = '{}'".format(d["username"])
    assert len(query(sql)) ==0
    
