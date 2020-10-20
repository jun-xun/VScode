# 循环  > 遍历
"""
username = "有世界的美丽"
j = 1
for i in username:
    print("这是第{}次运行, i的值是【{}】".format(j,i))
    j = j + 1


username = ("有","世","界","的","美","丽")
for i in username:
    print(i)


# 使用for 循环去取出1 这个数字
username = ["有","世","界","的","美","丽","hao",[1,2,5]]
for i in username:
    # 如何去判断 i 是最后一个元素
    if type(i) == list:
    # if type(i) == type(username):
        print(i[0])


username = {"name":"李白","skill":"sql","high":"170"}
for i in username:
    print(username[i])


account = [
        {"username":"游世杰", "password":"a12345678"}, 
        {"username":"刘军", "password":"a12345678"}
    ]
len(account) # 最后一次循环和account有什么关系?
j = 1
a = input("输入账号：")
b = input("输入密码：")
for i in account:
    if a == i["username"]:
        print("注册使用，用户已存在！")
        break
    else:
        if j == len(account):
            new_account = {"username":a, "password":b}
            account.append(new_account)
        # 判断是否为最后一个账号
            print("添加成功")
            break
    j = j + 1
print(account)


# 注册一个用户
# 如果用户已存在，那么打印注册使用，用户已存在
# 如果用户不存在，那么去添加一个用户信息
# 例子 ： 用户名：李白，a12345678 》成功：刘军》注册失败
account = [
        {"username":"游世杰", "password":"a12345678"}, 
        {"username":"刘军", "password":"a12345678"}
    ]
# len(account) # 最后一次循环和account有什么关系?
u = input("请输入用户名:")
j = 1 # 运行的次数 j > 2 刘军 > 最后一次 > len(account)
for i in account:
    print(i)
    if i["username"] == u:
        print("用户名已存在，注册失败")
        break
    else:
        # 判断是否为最后一个账号
        if j == len(account):
            print("用户名不存在，开始注册")
            new_user = {"username":u, "password":"a12345678"}
            account.append(new_user)
            # 终止循环
            break
    print("==========================================")
    j = j + 1
"""

a = [1,2,3]
for i in a:
    if i == 2:
        continue
    print(i)
    
# 打印 10 以内的奇数
for i in range(1,11):
    if i % 2 == 1:
        print(i)

# for i in range(1,11):
#     print(i)



