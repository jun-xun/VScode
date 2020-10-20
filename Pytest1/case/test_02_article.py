import pytest
import requests

# 跨文件夹导入，把根目录变成环境变量 
import os, sys
sys.path.append(os.getcwd())

from utils.dbtools import query
from utils.filetools import write_file,read_file
from conf.commontools import HOST
from conf.commontools import get_url

# 测试用例
def test_01_new_article():
    # u = "http://118.24.105.78:2333/article/new"
    u = HOST + "/article/new"
    u = get_url("/article/new")
    h = {"Content-Type":"application/json","token":read_file("./conf/user_token.txt")}
    d = {"title":"不学习没饭吃", "content":"楞个慢", "tags":"海上生明月", "brief":"介绍", "ximg":"dsfsdf.jpg" }
    r = requests.post(url=u,headers=h,json=d)

    assert r.status_code ==200
    assert r.json()["status"] ==200   
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