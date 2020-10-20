from selenium import webdriver
import requests


# 包和文件在同级目录下
from test.a import username
print(username)

# 同级别文件的 相互导入
from day04demo import password
print(password)


# 同级别文件的 相互导入
from dbtools import query
sql = 'select * from orders'
r = query(sql)
print(r)