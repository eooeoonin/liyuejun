# 引入包
# 求和
# 方式一
# from pack01.fonc1 import sum1  # from 包名.模块名 import 函数名（方法名） 使用时直接用方法名即可，如果引用多个方法用逗号隔开
# a=int(input("求1--n的和请输入数字："))
# b=sum1(a)
# print(b)
# 方式二
# from pack01 import fonc1  # from 包名 import 模块名  使用对应方法时，要用模块名.方法名引用
# a=int(input("求1--n的和请输入数字："))
# b=fonc1.sum1(a)
# print(b)


from pack01.fonc1 import denglu
# 登录
user2=input("请输入用户名：").strip()
pawd2=input("请输入密码：").strip()
login=denglu(user2,pawd2)
print(login)  #打印才能显示返回值



