import unittest
from utils.HTMLTestRunner import HTMLTestRunner

# 查找所有的测试用例
testcases = unittest.defaultTestLoader.discover("case","test_*.py")

# 使用 HTMLTestRunner 去自动运行所有的测试用例
# 并且生成所有的测试报告
title = "测试报告第1次测试"
descr = "这就是测试报告"
filepath = "./report/report.html"
with open(filepath, "wb") as f:
    runner = HTMLTestRunner(stream=f, title=title, description=descr)
    runner.run(testcases)
