import time # 导入包


a = 1
b = 2
while b > a:
    # print("是的")
    a = a + 1

"""
 红绿灯
 使用python 打印红绿灯，红绿灯打印30次，绿灯打印25次，黄灯5次
"""
while True:   
    for i in range(60):  # 0-29:打印红灯， 30-54：打印绿灯， 55-59：打印黄灯
        if i < 30:
            print("红灯")
        if i > 29 and i < 55:
            print("绿灯")
        if i > 54:
            print("黄灯")
        time.sleep(1)
