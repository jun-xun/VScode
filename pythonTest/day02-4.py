# account = {"username":"junxun","password":"a123456"}
# username = input("请输入你的账号：")
# password = input("请输入你的密码：")

# if username == account["username"] and password == account["password"]:
#     print("登录成功！")
# else:
#     print("账号密码错误！请检查账号密码是否正确")


# account = {"username":"test"}
# username = input("请输入你的账号：")

# if username == account["username"]:
#     account["password"] = "12345678"
#     print(account)
# else:
#     print("账号不对")

a = int(input("请输入你的年龄："))
if a < 18:
    print("{} < 18".format(a))
elif a < 20:
    print("18 <= {} < 20".format(a))
else:
    print("{} >= 20".format(a))
