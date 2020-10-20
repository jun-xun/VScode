from dbtools import query
from dbtools import commit


# 用户注册 测谈网 
username = input("请输入账号：")
password = input("请输入密码：")

sql = "select * from t_pymysql_account where username='{}'".format(username)
r = query(sql)
a = query(sql)
if len(r) != 0:
    print("该账号已注册，请重新输入账号")
else:
    sql = "insert into t_pymysql_account (username,password) values ('{}',{})".format(username, password)
    commit(sql)
    print("注册成功！")

# 登录测谈网的场景
# username = input("请输入账号：")
# password = input("请输入密码：")

sql = "select * from t_pymysql_account where username='{}' and password='{}'".format(username, password)
r = query(sql)
a = query(sql)
if len(r) != 0:
    print("登陆成功")
else:
    print("登陆失败")


