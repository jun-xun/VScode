# print("Hello Python World!")

# a = input("请输入年龄：")   # a = 我们输入的年龄
# print(a)

# 数据类型
# int
123

# float
123.123

# 字符串
a = "小团团你好呀"
b = '你好，小摩托'
c = """你好"""
r = a+ b
r1 = "x加{}".format("y")
# 把 y 拼接 到 {}, 花括号的内容 = 后面括号的内容
print(r1)
r6 = "{}加{}".format("zz","y")
print(r6)
  



# 字符串查找
r2 = a.find("大") # 找到了就返回查找内容在字符串中的位置
print(r2)
# 找到就返回下标，没找到就返回-1 

# 统计字符串出现的次数
r2 = a.count("团")
print(r2)

r2 = b.count("摩")
print(r2)

# # 替换字符串
r3 = a.replace("小","大")
# print(r3)

r3 = b.replace("摩托","明星")
print(r3)

# 获取字符串的下标
# print(a.index("小"))

# 获取字符串长度
# print(len(a))

# 布尔类型 bool
# Ture  # 真
# False # 假

# 空 NoneType
None

# list 数组，增/删/改/查
a = [1,2,3,3,3,"饭团"]
# 下标取值
print(a[0])
#增加
a.append("小摩托")
print(a)

# 修改
a[-1] = "大团团"
print(a)

# 删除
a.remove("饭团")
print(a)

# 统计个数
print(a.count(3))

# 数组排序
b = [1,34,21,11,9,66]  # 需要从小到大排序
b.sort()
print(b)

b = [1,34,21,11,9,66]  # 需要从大到小排序
b.sort(reverse=True)
print(b)

# tuple 元组，元素，下标取值
# a = (1,2,"3",True,None)
# print(a[0])
# print(a[1])
# print(a[-1])
# print(len(a))



# dict 字典
{"xm":"周杰伦","yz":"高","唱歌":"YES"}
{"name":"Tom","sex":"man","age":"19"}
{"banji":"2班","teacher":"李老师"}
{"bn":"建设","hl":"没懂"}
{"student":"李健","fee":"2000"}

# a = 1*2
# type(print(a))

