from selenium import webdriver

class BasePage(object):
    def __init__(self):
        self.driver = webdriver.Firefox()

# 打开浏览器
    def dakai(self,url):
        self.driver.get(url)
# 关闭浏览器
    def guanbi(self):
        self.driver.quit()

# 输入文本
    def shuru(self,selector,context):
        self.driver.find_element(*selector).send_keys(context)
#点击
    def dianji(self,selector):
        self.driver.find_element(*selector).click()