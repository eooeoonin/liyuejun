from xiangmu2.gongneng.jichu import jichugongneng
import time
class dengluye(jichugongneng):
    # 页面元素
    wangzhi="http://115.28.108.130/newecshop/admin/privilege.php?act=login" #网址
    username1=("name","username") # 用户名
    password1=("name","password") # 密码
    denglubutton=("class name","button2") #登录按钮


    def do_denglu(self,username,password):
        self.dakai(self.wangzhi)
        time.sleep(1)
        self.shuru(self.username1,username)
        self.shuru(self.password1,password)
        self.dianji(self.denglubutton)
        time.sleep(1)
        self.huoqudangqian()
        return self.huoqudangqian()

if __name__=="__main__":
    lp=dengluye()
    # lp.dakai("http://115.28.108.130/newecshop/admin/privilege.php?act=login")
    # time.sleep(1)
    lp.do_denglu("admin","hulaoshi2022")