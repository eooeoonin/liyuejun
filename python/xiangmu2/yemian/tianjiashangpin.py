from xiangmu2.gongneng.jichu import jichugongneng
import time

class tianjiaxinshangpinye(jichugongneng):
    #页面元素
    shangpinmingcheng=("name","goods_name") #商品名称位置
    shangpinfenlei1=("id","cat_name") #商品分类位置
    shangpinfenlei2=("id","treeDemo_cat_id_7_switch") #商品分类一级
    shangpinfenlei3=("link text","手机配件") #商品分类二级
    kuozhanfenlei1=("name","other_cat[]") #扩展分类位置
    kuozhanfenlei2="162" #扩展分类value值
    bendianshoujia=("name","shop_price") #本店售价位置
    queren=("id","goods_info_submit") #确认按钮位置

#输入商品名称
    def shangpinmingcheng(self,context):
        self.shuru(self.shangpinmingcheng,context)

#选择商品分类
    def shangpinfenlei(self):
        self.dianji(self.shangpinfenlei1)
        time.sleep(1)
        self.dianji(self.shangpinfenlei2)
        time.sleep(1)
        self.dianji(self.shangpinfenlei3)

#扩展分类
    def kuozhanfenlei(self):
        self.xuanzevalue(self.kuozhanfenlei1,self.kuozhanfenlei2)

#本店售价
    def bendianshoujia(self,shoujia):
        self.shuru(self.bendianshoujia,shoujia)

#点击确认
    def queren(self):
        self.dianji(self.queren)


