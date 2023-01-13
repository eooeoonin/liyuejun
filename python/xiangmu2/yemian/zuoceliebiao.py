from xiangmu2.gongneng.jichu import jichugongneng
import time
from xiangmu2.yemian.denglu import dengluye

class liebiao(jichugongneng):

    #页面元素
    shangpinguanliframe=("xpath",'//*[@id="menu-frame"]') #商品管理frame
    shangpinguanli=("xpath","/html/body/div/ul/li/ul/li[1]/a") #商品管理元素
    shangpinliebiao=("link text","商品列表") #商品列表元素
    tianjiaxinshangpin=("xpath",'/html/body/div/ul/li/ul/li[2]/ul/li[3]/a') #添加新商品元素

#点击商品管理
    def do_shangpinguanli(self):
        time.sleep(1)
        self.qiehuanframe(self.shangpinguanliframe)
        self.dianji(self.shangpinguanli)
        time.sleep(1)
#点击添加新商品
    def do_tianjiaxinshangpin(self):
        self.dianji(self.tianjiaxinshangpin)
        self.tuichuframe()
        time.sleep(1)
if __name__=="__main__":
    lp=dengluye()
    lp.do_denglu("admin","hulaoshi2022")
    liebiao().do_shangpinguanli()

