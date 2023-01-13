import unittest
from xiangmu2.yemian.denglu import dengluye
from xiangmu2.yemian.zuoceliebiao import liebiao
from xiangmu2.yemian.tianjiashangpin import tianjiaxinshangpinye

class MyTestCase(dengluye,liebiao,tianjiaxinshangpinye):
    @classmethod
    def setUpClass(cls):
        cls.do_denglu("admin","hulaoshi2022") #登录
        cls.do_shangpinguanli() #点击商品管理
        cls.do_tianjiaxinshangpin() #点击添加新商品

    def test_01(self): #商品名称为空
        self.shangpinmingcheng()
        self.shangpinfenlei()
        self.bendianshoujia(1000)
    def test_02(self):  # 商品分类为空
        self.shangpinmingcheng("小米手机")
        self.bendianshoujia(1000)
    def test_03(self):  # 本店售价为空
        self.shangpinmingcheng("小米手机")
        self.shangpinfenlei()
    def test_04(self):  # 必填项都填写（商品名称、商品分类、本店售价）
        self.shangpinmingcheng("小米手机")
        self.shangpinfenlei()
        self.bendianshoujia(1000)

    def tearDown(self):
        self.guanbi()
if __name__ == '__main__':
    unittest.main()
