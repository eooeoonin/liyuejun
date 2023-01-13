# 基础功能
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
import time
class jichugongneng(object):


    def __init__(self):
        # self.options = webdriver.ChromeOptions()
        # self.options.add_experimental_option('detach', True)  # 不自动关闭浏览器
        # self.options.add_argument('--start-maximized')  # 浏览器窗口最大化
        # self.driver = webdriver.Chrome(options=self.options)  # 创建一个谷歌方法给dr
        self.driver = webdriver.Firefox()
# 打开网页
    def dakai(self,url):
        self.driver.get(url)
#关闭网页
    def guanbi(self):
        self.driver.quit()
#点击
    def dianji(self,selector):
        self.driver.find_element(*selector).click()
#输入
    def shuru(self,selector,context):
        self.driver.find_element(*selector).clear()
        self.driver.find_element(*selector).send_keys(context)
#上传文件
    def shangchuan(self,selector,context):
        self.driver.find_element(*selector).send_keys(context)
#删除属性
    def shangchushuxing(self,selector,context):
        self.a=self.driver.find_element(*selector)
        self.js='arguments[0].removeAttribute("context")'
        self.driver.execute_script(self.js, self.a)
#截图
    def jietu(self,lujing):
        self.driver.get_screenshot_as_file(lujing)
#悬停
    def xuanting(self,selector):
        self.b=self.driver.find_element(*selector)
        ActionChains(self.driver).move_to_element(self.b).perform()

#value值选择
    def xuanzevalue(self,selector,value):
        self.c = self.driver.find_element(*selector)
        Select(self.c).select_by_value(value)
#切换frame
    def qiehuanframe(self,frameselector):
        self.d = self.driver.find_element(*frameselector)
        time.sleep(1)
        self.driver.switch_to.frame(self.d)
# 退出frame
    def tuichuframe(self):
        self.driver.switch_to.default_content()
# 获取当前页面
    def huoqudangqian(self):
        self.hand = self.driver.window_handles
        self.driver.switch_to.window(self.hand[0])

if __name__=="__main__":
    lp=jichugongneng()
    a=("xpath",'//*[@id="menu-frame"]')
    lp.qiehuanframe(a)