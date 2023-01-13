# 新增商品
import unittest

class goodtest(unittest.TestCase):
# 函数必须以test开头，函数执行顺序和函数名的数字顺序一致。先排数字，再排字母
    @classmethod
    def setUpClass(cls): # 在所有用例执行之前执行
        print("setUpClass")
    def setUp(self): #再每个用例之前执行
        print("setUp")
    def test_01(self):
        a=123
        self.assertEqual("abc",a)  # 断言--相等 前面为期望结果  后一个是实际结果
    def test_03(self):
        b="xyz"
        self.assertIn(b,"xyzabc") # 断言--包含，前一个值是不是在后面"xyzabc"里
    def test_abc(self):
        print("4444")
    def test_02(self):
        print("333")
    def tearDown(self): # 在每个用例之后执行
        print("tearDown")
    @classmethod
    def tearDownClass(cls): # 在所有用例执行之后执行
        print("tearDownClass")
if __name__ == '__main__':
    unittest.main()



