# 加入购物车自动化脚本
from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
dr=webdriver.Firefox()
# 打开网页
dr.get("http://115.28.108.130/newecshop/?u=63")
time.sleep(3)
# 选择一个分类手机、数码、通信--》iPhone
a=dr.find_element("xpath",'/html/body/div[3]/div/div[3]/div[2]/dl/dt/a')
ActionChains(dr).move_to_element(a).perform()
time.sleep(2)
dr.find_element("xpath",'/html/body/div[3]/div/div[3]/div[2]/div/div[1]/div[13]/dl[1]/dd/a[2]').click()
time.sleep(2)
# 切换窗口到新页面
hand=dr.window_handles
dr.switch_to.window(hand[1])
#选择一个商品加入购物车
dr.find_element("xpath",'/html/body/div[5]/div[4]/div[2]/form[1]/ul/li[1]/div/div[3]/div[3]/a[4]').click()
time.sleep(1)
# 弹窗选择商品属性
dr.find_element("xpath",'/html/body/div[14]/div[2]/div[2]/span[2]/label').click()
time.sleep(1)
dr.find_element("xpath",'/html/body/div[14]/div[3]/a[1]').click()
time.sleep(1)
# 打开购物车列表
dr.find_element("xpath",'/html/body/div[6]/div/div[1]/div[1]/ul/li[3]/div/div').click()



