# 跑批量，生成报告
from unittest_xuexi import htmlrunner
import unittest
from unittest_xuexi.addgoods import goodtest
su=unittest.TestSuite() # 建一个批量跑的套件
fp= open("C:\\Users\\CYP-USERS\\Desktop\\xuexi\\report.html",'wb') # 新建一个报告文件
runner= htmlrunner.HTMLTestRunner(fp,title="测试报告2022") # 新建一个对象
su.addTest(goodtest("test_01"))
su.addTest(goodtest("test_03"))
runner.run(su)
fp.close()