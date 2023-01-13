# 后台商品列表删除一个商品
from selenium import webdriver
import time
# 打开网址，登录
dr=webdriver.Firefox()
dr.get("http://115.28.108.130/newecshop/admin/privilege.php?act=login")
time.sleep(2)
dr.find_element("name","username").send_keys("admin")
dr.find_element("name","password").send_keys("hulaoshi2022")
time.sleep(1)
dr.find_element("class name","button2").click()
# 点击商品列表
dr.switch_to.frame(dr.find_element("xpath",'//*[@id="menu-frame"]'))
dr.find_element("xpath","/html/body/div/ul/li/ul/li[1]/a").click()
time.sleep(1)
dr.find_element("link text","商品列表").click()
dr.switch_to.default_content()
# 输入关键字搜索
dr.switch_to.frame(dr.find_element("xpath",'//*[@id="main-frame"]'))
time.sleep(1)
dr.find_element("name","keyword").send_keys("橙子")
dr.find_element("xpath",'/html/body/div[2]/form/input[4]').click()
time.sleep(1)
# 删除第一个商品
dr.find_element("xpath",'/html/body/form/div[1]/table[1]/tbody/tr[3]/td[13]/a[4]/img').click()
time.sleep(1)
alert1=dr.switch_to.alert
time.sleep(1)
alert1.accept()


