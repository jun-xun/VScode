import pytest
import requests

# 跨文件夹导入，把根目录变成环境变量 
import os, sys
sys.path.append(os.getcwd())

from utils.dbtools import query
from utils.filetools import write_file,read_file
from utils.commontools import HOST
from utils.commontools import get_url
from utils.exceltools import read_excel

data = read_excel(excel_path="data\测谈网接口测试用例.xlsx", sheet_name='文章模块')

# 测试用例
def test_01_new_article():
    # u = "http://118.24.105.78:2333/article/new"
    # u = HOST + "/article/new"
    u = eval(data[0][2])  # 因为返回的 data 数据是字符串类型，这里的 eval 把字符串转换成对应的类型
    h = eval(data[0][3])  # eval 把字典类型的字符串转换成 字典
    d = eval(data[0][4])
    r = requests.post(url=u,headers=h,json=d)

    assert r.status_code ==int(data[0][5])
    assert r.json()["status"] ==int(data[0][6])
    # print(r.text)

    iid = r.json()["data"]["articleid"]
    sql = "select * from t_article where id ='{}'".format(iid)
    assert len(query(sql)) != 0
    write_file("./conf/article_id.txt",str(iid))  # 写都是字符串类型，这里的文章id 是int 类型，所以要转换成字符串类型
    # print(query(sql))



# import requests

# url = "http://118.24.105.78:2333/logou"

# payload = {}
# headers = {
#   'Content-Type': 'application/json',
#   'token': '86112a48f04867a83f68ab21nuyuil67a47b5b3d4536ad0'
# }

# response = requests.request("GET", url, headers=headers, data = payload)

# print(response.text.encode('utf8'))