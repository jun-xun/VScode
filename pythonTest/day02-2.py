a = 1
b = "1"
print(type(b))
# 1.数字转字符串
c = str(123)
print(type(c))
# 2. 字符串转数字
d = int(b)
print(type(d))

# e = "aa"
# int(e)

# 元组和数组
cc = (1,2,3,4)
dd = list(cc)
print(dd)
ee = tuple(dd)
print(ee)

 # 字符串>字典，eval，强制转换类型
q = "{'username':'你好'}" # 字典格式的字符串
o = "(1,2,3)"
print(type(eval(q)))   #把对应的字符串格式转换成对应的类型, 就是只变了输出后的类型
#    eval 的作用：把 字典格式的字符串 "{'username':'你好'}" 转换成字典 {'username':'你好'}
print(type(eval(o)))

a = input("请输入一个文字：")
b = "网吧五连坐"
c = ("从来没赢过",123)
d = ["从来没赢过",123]
if a in c:
    print("找到了")
else:
    print("没找到")