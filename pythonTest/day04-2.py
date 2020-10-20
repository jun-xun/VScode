# 方法
# def jiafa(s1,s2,s3=11):
#     sum = s1 + s2 +s3
#     return sum
# a = jiafa(1,9)
# print(a)

# def multiplication(a1,a2,a3):
#     b = a1 * a2 * a3
#     return b
# c = multiplication(2,3,4)
# print(c)


# a = jiafa(1,9)
# b = jiafa("a","b")
# print(a)
# print(b)

from selenium import webdriver
import requests

from dbtools import query
sql = "select * from orders"
r = query(sql)
print(r)