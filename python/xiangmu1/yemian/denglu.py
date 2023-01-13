from selenium.webdriver.common.by import By
from xiangmu1.jichu.BasePage import BasePage
import time
class denglu(BasePage):
    # 定义页面全部元素
    username=(By.XPATH,"/html/body/div/form/table/tbody/tr/td/table/tbody/tr[1]/td[2]/input") #用户名输入框
    password=(By.XPATH,"/html/body/div/form/table/tbody/tr/td/table/tbody/tr[2]/td[2]/input") #密码输入框
    loginbtn=(By.XPATH,"/html/body/div/form/table/tbody/tr/td/table/tbody/tr[4]/td/input") #登录按钮

    def do_denglu(self,username,password):
        self.shuru(self.username,username)
        self.shuru(self.password,password)
        self.dianji(self.loginbtn)



if __name__=="__main__":
    lp=denglu()
    lp.dakai("http://115.28.108.130/newecshop/admin/privilege.php?act=login")
    time.sleep(1)
    lp.do_denglu("admin","hulaoshi2022")