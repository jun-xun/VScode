# 字典，键值对，key-value, key不能重复
a = {"xm":"周杰伦","sy":"高","唱歌":"YES","age":"28","gf":["冰冰","林志玲","利好"]}

print(a["xm"])
print(a.get("xm"))
# print(len(a))
# # 取值：a[""]如果取不存在的key,会报错；get方法默认的是None
# b = a["xm"]
# c = a.get("sy")
# print(a["xm"])

# # 增加
# a["sg"] = 190
# print(a)

# # 修改
# a["sg"] = 180
# print(a)
# #如果key 存在，就是修改;不存在，就是新增

# # 删除; 删除某个键值对
# del a["sg"]
# print(a)

# # 全部删除
# del a
# a.clear()
# print(a)