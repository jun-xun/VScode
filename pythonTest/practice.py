print("Hello Python World!")

# a = input("请输入你的年龄：")
# print("你的年龄为："+ a)

# int
123
# float
123.333

# 运算
a = 1.3 + 2.5
b = 2*2
c = a + b
print(a)
print(b)
print(c)


# 字符串
a = "软件测试很有趣"
b = "小电电电驴"
c = "永远有电"

# 字符串拼接
r = a + b
print(r)
r1 = "x加{}".format(1)
print(r1)

# 获取字符串的长度
print(len(a))
# 获取某个字符在字符串中的位置（下标）
print(a.index("有"))

# 替换字符串
cl = a.replace("有","无")
print(cl)

# 字符串查找
r2 = a.find("啊哈哈") # 找到了就返回查找内容在字符串中的位置
print(r2)
# 没找到就返回-1

# 统计字符出现的次数
r3 = b.count("电")
print(r3)

# tuple 元组，元素，下表取值
a = (9,2,5,66,7,33,11,"全村跳舞")
print(a[0])
print(a[1])
print(a[-1])
print(a[-2])
print(a[3])

# list 数组,增/删/查/改
g = [99,6,"浪哥","流云"] 

# 取值
print(g[0])
print(g[-1])

# 增
r4 = g.append("希希")
print(g)

# 删
g.remove(6)
print(g)

# 改
g[0] = "大雁塔"
print(g[0])

# 统计个数
print(g.count("浪哥"))

cc = [1,22,9,6,10,99]
cc.sort() # 从小到大 排序
print(cc)

cc.sort(reverse=True) # 从小到大 排序
print(cc)