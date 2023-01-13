"""
web 自动化 qtp selenium lr(loadrunn)
app 自动化
接口自动化
"""
from selenium import webdriver # 导入包
from selenium.webdriver.support.ui import Select #导入select标签包
import time #导入时间包
# dr=webdriver.Firefox() #创建一个火狐方法给dr 需要驱动放在python安装路径里geckodriver.exe
# chrome 需要加下面代码，程序运行完不自动关闭
options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)  #不自动关闭浏览器
options.add_argument('--start-maximized')#浏览器窗口最大化
dr=webdriver.Chrome(options=options) #创建一个谷歌方法给dr
# dr.get("http://115.28.108.130/newecshop/admin/privilege.php?act=login")
#

# dr.get("https://www.baidu.com") # 打开狐火浏览器，依赖geckodriver驱动
# dr.find_element("id","kw").send_keys("龙腾") #找到元素，用id这个属性定位，属性值为kw，然后发送给键盘，输入“龙腾”
# 没有id定位，a 标签中用link text 超文本链接
# dr.find_element("link text","新闻").click() #用超文本链接找到新闻，点击
# dr.get("http://sahitest.com/demo/index.htm")
# time.sleep(3) #等3秒
# dr.find_element("link text","Select Test").click()
# select标签 使用前提需要导入Select包 查找select标签中的id，value是html中select标签下选项的属性
# Select(dr.find_element("id","s2Id")).select_by_value("o1")
# 如果value值是一样的，需要用by_visible_text("对应选项内容") 如果是nbsp输入不能忽略
# Select(dr.find_element("id","s3Id")).select_by_visible_text("    With nbsp")
# 如果是空格，by_visible_text()中输入忽略空格
# Select(dr.find_element("id","s3Id")).select_by_visible_text("With spaces")
# dr.back() 返回
# dr.forward() 前进

# dr.get("file:///C:/Users/CYP-USERS/Desktop/xuexi/control.html")
# time.sleep(1)
# dr.find_element("link text","百度首页走起~").click()
# dr.find_element("partial link text","百度首页").click() # 部分包含
# time.sleep(1)
# dr.back()
# dr.find_element("name","account").send_keys("liyuejun")
# dr.find_element("name","password").send_keys("123456")
# Select(dr.find_element("id","areaID")).select_by_value("3")
# dr.find_element("id","sexID2").click()
# dr.find_elements("id","u")[2].click() # 找到所有id为u的元素，存放在一个列表里
# dr.find_element("id","check").send_keys("11111")
# dr.find_element("class name","stuname").send_keys("abcd") #class标签要用class name名字

#Xpath语法 万能方法，没有标签限制和属性限制
# /html/body/div[3]/input 绝对路径
# //input[@id="passwordID"] # 相对路径 找input标签中属性是id="passwordID"的
# //*[@id="accountID"] 可以用f12后，选中需要的标签，右键复制选择Xpath

# dr.get("file:///C:/Users/CYP-USERS/Desktop/xuexi/control.html")
# time.sleep(1)
# dr.find_element("xpath",'//input[@id="check"]').send_keys("abcd")
# dr.find_element("xpath",'//*[@value="winter"]').click()
# dr.find_element("xpath",'//*[@id="u" and @value="Auterm"]').click() #用两个属性定位
# dr.find_element("xpath",'/html/body/div[1]/form/table/tbody/tr[5]/td/input[1]').click() #根据绝对路径
# dr.find_element("xpath",'//input[2][@id="u"]').click()
# 找到id为u的所有元素，都点击
# for i in dr.find_elements("id","u"):
#     i.click()


# frame/iframe 先要切换到对应的frame或iframe，然后再操作里面的元素
# dr.get("http://sahitest.com/demo/index.htm")
# time.sleep(3)
# dr.find_element("link text","IFrames Test").click()
# time.sleep(3)
# dr.switch_to.frame(dr.find_element("xpath","/html/body/iframe"))
# dr.find_element("link text","Table Test").click()
# 跳出frame
# dr.switch_to.default_content() #跳出所有frame
# time.sleep(3)
# dr.switch_to.frame(dr.find_element("xpath","/html/body/div/iframe"))
# dr.find_element("link text","Link Test").click()
# switch_to.parent_frame() #切到父文档(相当于后退)

# 弹窗alert
# dr.get("http://sahitest.com/demo/index.htm")
# time.sleep(3)
# dr.find_element("link text","Alert Test").click()
# time.sleep(1)
# dr.find_element("name","b1").click()
# alert1=dr.switch_to.alert
# time.sleep(1)
# alert1.accept() #相当于点确认按钮
# time.sleep(1)
# dr.back()
# dr.find_element("link text","Confirm Page").click()
# time.sleep(1)
# dr.find_element("name","b1").click()
# time.sleep(1)
# alert2=dr.switch_to.alert
# time.sleep(1)
# alert2.dismiss() #取消
# time.sleep(1)
# dr.back()
# dr.find_element("link text","Prompt Page").click()
# time.sleep(1)
# dr.find_element("name","b1").click()
# time.sleep(1)
# alert3=dr.switch_to.alert
# alert3.send_keys("liyuejun") #在弹窗中输入值
# time.sleep(1)
# alert3.accept()

# 切换窗口
# dr.get("http://sahitest.com/demo/index.htm")
# time.sleep(3)
# dr.find_element("link text","Window Open Test").click()
# time.sleep(1)
# hand=dr.window_handles
# print(dr.current_url)
# dr.switch_to.window(hand[1])
# print(dr.current_url)
# print(hand)
# dr.switch_to.frame(dr.find_element("xpath",'/html/frameset/frame[1]'))
# dr.switch_to.frame("top") #当这个frame 有id ,name 的时候  ，frame 括号里面可以直接写name 或者的id的属性值
# dr.find_element("link text","Table Test").click()
# time.sleep(1)
# dr.back()
# time.sleep(1)
# dr.switch_to.default_content()
# dr.switch_to.frame(dr.find_element("xpath",'/html/frameset/frame[2]'))
# dr.find_element("link text","Link Test").click()
# time.sleep(1)

# 模拟键盘
# from selenium.webdriver.common.keys import Keys
# dr.get("http://sahitest.com/demo/index.htm")
# time.sleep(2)
# dr.find_element("link text","Key Press").click()
# time.sleep(1)
# dr.find_element("name","t2").send_keys(Keys.ENTER) #enter键
# time.sleep(1)

# 模拟鼠标
from selenium.webdriver.common.action_chains import ActionChains
# dr.get("http://sahitest.com/demo/index.htm")
# time.sleep(2)
# 鼠标悬停
# dr.find_element("link text","Mouse over").click()
# time.sleep(1)
# a=dr.find_element("xpath",'/html/body/form/input[1]') #找到定位元素
# ActionChains(dr).move_to_element(a).perform() #移动到对应元素上悬停
# 拖拽
# dr.find_element("link text","Drag Drop Test").click()
# time.sleep(1)
# b=dr.find_element("id","dragger")
# c=dr.find_element("xpath",'/html/body/div[3]')
# d=dr.find_element("xpath",'/html/body/div[5]')
# ActionChains(dr).drag_and_drop(b,c).perform()
# time.sleep(1)
# ActionChains(dr).drag_and_drop(b,d).perform()

# 上传文件
# f=dr.find_element("name","goods_img")
# f.send_keys("C:\\Users\\CYP-USERS\\Desktop\\xuexi\\python\\Dingtalk_20221215202608.jpg")

# js交互 删除属性
# e1=dr.find_element("id","promote_start_date") #找到促销日期元素
# js1='arguments[0].removeAttribute("readonly")'  #删除readonly属性
# dr.execute_script(js1,e1) #执行删除e1的属性
# dr.find_element("id","promote_start_date").clear()
# dr.find_element("id","promote_start_date").send_keys("2022-12-30 10:13")


# 截图操作
# save_fn="C:\\Users\\CYP-USERS\\Desktop\\xuexi\\python\\截图1.png"
# dr.get_screenshot_as_file(save_fn)

# save_fn="C://Users//CYP-USERS//Desktop//xuexi//python//截图1.png"
# dr.get_screenshot_as_file(save_fn)


# is_displayed()：判断元素是否被展示出来
#
# is_enabled()：判断元素是否可操作
#
# is_selected()：判断元素是否被选择

#element = puCom.element._find_element(TeacherClassManageObj.input_enName) //先找到该元素，其中，input_enName ="//div[@id='bodyContainer']//input[@id='enName']"

#act_enName = puCom.sLib._current_browser().execute_script("return arguments[0].value", element) //js获取当前元素的value值


#等待元素
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
#输入文本
wait.until(ec.visibility_of_element_located((By.XPATH,'/html/body/div[6]/div/div[1]/div[1]/ul/li[3]/div/div'))).send_keys("111")
#点击
wait.until(ec.element_to_be_clickable((By.XPATH,'//[@id=“Subnet”]'))).click()



























