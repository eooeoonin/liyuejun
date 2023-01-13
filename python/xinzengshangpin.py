# 新增商品自动化脚本
from selenium import webdriver
from selenium.webdriver.support.ui import Select
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
# 点击新增商品按钮
dr.switch_to.frame(dr.find_element("xpath",'//*[@id="main-frame"]'))
time.sleep(2)
dr.find_element("xpath",'/html/body/h1/span[1]/a').click()
time.sleep(1)
# 填写商品通用信息
# 商品名称
dr.find_element("name","goods_name").send_keys("蓝牙耳机(lyj)")
# 商品分类
dr.find_element("id","cat_name").click()
time.sleep(1)
dr.find_element("id","treeDemo_cat_id_7_switch").click()
time.sleep(1)
#dr.find_element("xpath",'//*[@id="treeDemo_cat_id_8_switch"]').click()
dr.find_element("link text","手机配件").click()
# time.sleep(1)
# dr.find_element("link text","蓝牙耳机").click()
time.sleep(1)
# 扩展分类
Select(dr.find_element("name","other_cat[]")).select_by_value("162")
time.sleep(1)
# 商品品牌
dr.find_element("id","brand_search").click()
dr.find_element("link text","姬芮").click()
time.sleep(1)
# 选择供货商
Select(dr.find_element("id","suppliers_id")).select_by_value("1")
# 本店售价
dr.find_element("name","shop_price").clear() # 清空输入框内容
dr.find_element("name","shop_price").send_keys("123.98")
time.sleep(1)
# 按市场价计算
dr.find_element("xpath",'/html/body/div[2]/div[2]/form/table[1]/tbody/tr[7]/td[2]/input[2]').click()
# 手机专享价
dr.find_element("name","exclusive").clear()
dr.find_element("name","exclusive").send_keys("120")
time.sleep(1)
# 会员价格
dr.find_element("id","rank_1").clear()
dr.find_element("id","rank_1").send_keys("124")
# 商品优惠价格
dr.find_element("name","volume_number[]").send_keys("10")
dr.find_element("name","volume_price[]").send_keys("120")
# 赠送消费积分数
dr.find_element("name","give_integral").clear()
dr.find_element("name","give_integral").send_keys("20")
# 赠送等级积分数
dr.find_element("name","rank_integral").clear()
dr.find_element("name","rank_integral").send_keys("10")
# 促销价
dr.find_element("id","is_promote").click()
dr.find_element("name","promote_price").clear()
dr.find_element("name","promote_price").send_keys("100")
time.sleep(1)
# 设置促销日期
# dr.find_element("id","promote_start_date").click()
# dr.switch_to.frame(dr.find_element("xpath",'/html/body/div[6]/iframe'))
# dr.find_element("xpath",'//*[@id="dpTodayInput" and @value="今天"]').click()
# dr.switch_to.parent_frame()
# dr.find_element("id","promote_end_date").click()
# dr.switch_to.frame(dr.find_element("xpath",'/html/body/div[6]/iframe'))
# dr.find_element("xpath",'/html/body/div/div[3]/table/tbody/tr[6]/td[4]').click()
# dr.find_element("xpath",'//*[@id="dpOkInput"]').click()
# dr.switch_to.parent_frame()

# 设置促销日期 JS交互，删除属性
e1=dr.find_element("id","promote_start_date") #找到促销日期元素
js1='arguments[0].removeAttribute("readonly")'  #删除readonly属性
dr.execute_script(js1,e1) #执行删除e1的属性
dr.find_element("id","promote_start_date").clear()
dr.find_element("id","promote_start_date").send_keys("2022-12-30 10:13")
time.sleep(1)
e2=dr.find_element("id","promote_end_date") #找到促销日期元素
js2='arguments[0].removeAttribute("readonly")'  #删除readonly属性
dr.execute_script(js2,e2) #执行删除e2的属性
dr.find_element("id","promote_end_date").clear()
dr.find_element("id","promote_end_date").send_keys("2023-1-30 11:15")
# 限购数量
dr.find_element("id","is_buy").click()
dr.find_element("id","buymax").send_keys("10")
# 限购日期
dr.find_element("id","selbtn3").click()
dr.find_element("xpath",'/html/body/div[7]/table/tbody/tr[5]/td[5]').click()
dr.find_element("id","selbtn4").click()
dr.find_element("xpath",'/html/body/div[8]/table/tbody/tr[5]/td[7]').click()
time.sleep(1)
# 分成
dr.find_element("name","cost_price").clear()
dr.find_element("name","cost_price").send_keys("10")
time.sleep(1)

# 上传商品图片
f=dr.find_element("name","goods_img")
f.send_keys("C:\\Users\\CYP-USERS\\Desktop\\xuexi\\python\\Dingtalk_20221215202608.jpg")
time.sleep(3)

# 截图操作
save_fn="C:\\Users\\CYP-USERS\\Desktop\\xuexi\\python\\截图1.png"
dr.get_screenshot_as_file(save_fn)

# save_fn="C://Users//CYP-USERS//Desktop//xuexi//python//截图1.png"
# dr.get_screenshot_as_file(save_fn)
# 详细描述
dr.find_element("id","detail-tab").click()
dr.find_element("xpath",'/html/body').click()
dr.find_element("xpath",'/html/body').send_keys("特别实用")
time.sleep(2)

# 确认
# dr.find_element("id","goods_info_submit").click()
