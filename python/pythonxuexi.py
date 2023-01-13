# 注销 （ctrl+/）
"""
注释
注释
注释
"""
# print("hello python") #打印输出
# 变量
# a=3
# b=2
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# 取余数
# print(b%a)
# a的b次方
# print(a**b)
# 取整
# print(b//a)
# a+=b
# a=a+b
# a-=b
# a=a-b
# print(a)
# 在python中，0代表假，false代表假，none代表假，其余都是真
# print(0 and 1)
# print(0 or 1)
# print(1 and 1)
# print(1 or 1)
"""
a=1
b="1"
c=1.1
d=[1,"xy","1.1",{"user":"liyuejun"}] # 列表
e={"code":"1",
   "msg":"\u767b\u5f55\u6210\u529f",
   "data":
    {"key":"7da8e09d9262030fdd77d99071afef93",
     "userid":"1135223",
     "data":"7da8e09d9262030fdd77d99071afef93",
     "expiry":"huxiaoyantest28e10adc3949ba59abbe56e057f20f883e1671157592",
     "time":1671157592
     }
   }
f={"code":"1",
   "msg":"\u83b7\u53d6\u7528\u6237\u4fe1\u606f\u6210\u529f",
   "data":
    [
        {"nick_name":"huxiaoyantest28",
         "sex":"0",
         "integration":"0",
         "address":None,
         "mobile":None,
         "email":"huxiaoyantest28@qq.com",
         "user_money":"0.00",
         "birthday":"0000-00-00",
         "consume":None,
         "attention":"0",
         }
    ]
   }
g=(1,"1.1","123") # 元组
print(type(a),type(b),type(c),type(d),type(e),type(f),type(g)) #type函数是告诉这个变量是什么类型
"""
# 字符串
# print("abc")
# print('"abc"')
# 转义字符\n(换行）\u(unicode码）
# print("a\nb")
# print("\u767b\u5f55\u6210\u529f")
# print("\\u767b\\u5f55\\u6210\\u529f")
"""
a="abcdefg李" # 字符串是一个序列，从0开始
b=a[7]
print(b)
print(a[7])
print(a[-1]) # 从逆向，从-1开始
"""
a="abcdef李"
# print(a[0:3]) #包含第0个，但不包含最后一个字符d
# in 判断一个字符串是否在另一个字符串中
# print("李" in a)
# print("z" in a)
# 拼接字符串 +（用在字符串中）
# print(a+"long")
# len 是内置函数，返回字符串中的字符个数
# print(len(a))
# 假设字符个数为奇数，输出中间字符
# print(a[len(a)//2])
# find函数 找出包含字符“cd“中的c，在字符串a中的位置输出来
# print(a.find("cd"))

# 列表 从0开始
# e=['d:', 'usr', 'local', 'bin']
# print(e[0],e[3])
list1=["1","d","xy"]
print(list1[2])

# split函数 是以什么方式（/）拆分，拆分后是列表形式输出
# path="d:/usr/local/bin"
# f=path.split("/")
# print(type(f))
# print(f)
# join函数 是合并列表f，如['d:', 'usr', 'local', 'bin']，以什么方式（//)合并
# g="//".join(f)
# print(g)

# strip函数 去掉最左边和最右边空格
# y="  a:b :c  xyz  "
# print(y)
# print(y.strip())

# 选择结构，条件判断 if else
# a=1
# if a:
#     print("xyz")
# else:
#     print("abc")
# b=0
# if b:
#     print("xyz")
# else:
#     print("abc")

# a="longtengabc"
# if "longteng" in a:
#     print("pass")
# else:
#     print("fail")
#
# b="longtengabc"
# if "longteng" not in b:
#     print("fail")
# else:
#     print("pass")

# 键盘输入方法 input()
# c=input("请输入:")
# print(c)
# a="longtengabc"
# if c in a:
#     print("pass")
# else:
#     print("fail")

# user="longteng"
# pawd="123456"
# 从键盘输入用户名和密码，假如输入正确，输出”登录成功“，错误输出”登录失败“
# user1=input("请输入用户名：")
# pawd1=input("请输入密码：")
# if (user1==user and pawd1==pawd):
#     print("登录成功")
# else:
#     print("登录失败")

# 选择结构 多条件判断 if(): elif(): else:
# a=100
# b=input("请输入：")
# print(type(b))
# c=int(b) # 转换成整数类型，必须输入的是数字
# if(c<a):
#     print(1)
# elif(c==a):
#     print(2)
# else:
#     print(3)


# user="longteng"
# pawd="123456"
# user1=input("请输入用户名：").strip()
# pawd1=input("请输入密码：").strip()
# if(user1=="" or pawd1==""):
#     print("用户名或密码不能为空")
# elif(user1==user and pawd1==pawd):
#     print("登录成功")
# else:
#     print("用户名和密码不匹配")

# 循环语句 while
# a=0
# while a<10:
#     print("longtengceshi")
#     a+=1
# print("over")

# 求100内能被3整除的数
# a=100
# while a>=0:
#     b=a%3
#     if (b==0):
#         print(a)
#         a-=1
#     else:
#         a-=1
# print("over")

# 100以内能被3整除且能被5整除
# a=100
# while a>=0:
#     if (a%3==0 and a%5==0):
#         print(a)
#     a=a-1
# print("over")

# a=100
# sum=0
# while a>=0:
#     if (a%3==0 and a%5==0):
#         sum=sum+a
#     a=a-1
# print(sum)

# 循环结构 for循环
# names="xyzab"
# for name in names:
#     print(name)
#     print("执行sample")

# range(0,10)代表0,1,2,3,4,5,6,7,8,9
# for i in range(0,10):
#     print(i)

# 求100内能被3整除的数
# for i in range(0,101):
#     if i%3==0:
#         print(i)
# 100以内能被3整除且能被5整除
# for i in range(0,101):
#     if i%3==0 and i%5==0:
#         print(i)

# 多重循环
# for i in "xyz":
#     print(i)
#     for j in "abc":
#         print(j)
# for i in "xyz":
#     for j in "abc":
#         print(i+j)
# 输出矩形
# for i in range(0,5):
#     if i!=0:
#         print(end="\n")
#     for j in range(0,5):
#         print("*",end=" ")
# 输出矩形
# for i in range(0,5):
#     for j in range(0,5):
#         print("*",end=" ")
#     print(end="\n")
# 输出三角形
# for i in range(1,6):
#     while i>0:
#         print("*", end=" ")
#         i=i-1
#     print("")
# 输出三角形
# for i in range(1,6):
#     for j in range(0,i):
#         print("*",end=" ")
#     print("")

# 格式化输出
# print(x,y) 输出两个，中间以空格隔开
# print("x","y")
#print("xyz") #默认输出一个换行符

# print("xyz","abc",end="") #end=""代表去掉换行符，直接与后面相连
# print("xyz")

# print("xyz","abc",end="，") #end="，"代表用，隔开，和后面相连
# print("xyz")

# break 跳出一个循环语句
# for a in "python":
#     if a=="h":
#         break
#     print(a)
# while True为真就一直循环
# while True:
#     a = input("请输入字符串:")
#     print(len(a))
#     if len(a)==3:
#         break


# 函数
# def jump():
#     print("我要打印100行代码")
# # 调用这个方法
# print(jump())

# 传参一个值
# def jump(x):
#     print(x+7)
# # 调用这个方法
# print(jump(8))

# 传参两个值
# def jump(x,y):
#     print(x+7+y)
# # 调用这个方法
# print(jump(8,1))

# return 如果为空返回none 函数只返回return 后的值
# def jump(x,y):
#     sum=x+y
#     return sum
# # 调用这个方法
# a=jump(8,1)+8
# print(a)

# 函数调用 这种不太符合逻辑，有参数的情况调用方法要传参数
# def denglu():
#     user="longteng"
#     pawd="123456"
#     user1=input("请输入用户名：").strip()
#     pawd1=input("请输入密码：").strip()
#     if(user1=="" or pawd1==""):
#         a=print("用户名或密码不能为空")
#     elif(user1==user and pawd1==pawd):
#         a=print("登录成功")
#     else:
#         a=print("用户名和密码不匹配")
#     return a
# denglu()

# 这种更符合使用逻辑
# def denglu(user1,pawd1):
#     user="longteng"
#     pawd="123456"
#     if(user1=="" or pawd1==""):
#         return "用户名或密码不能为空"
#     elif(user1==user and pawd1==pawd):
#         return "登录成功"
#     else:
#         return "用户名和密码不匹配"
#
#参数一一对应，位置一致
# user2=input("请输入用户名：").strip()
# pawd2=input("请输入密码：").strip()
# login=denglu(user2,pawd2)
# print(login)  #打印才能显示返回值

#参数名一致，位置无关
# user2=input("请输入用户名：").strip()
# pawd2=input("请输入密码：").strip()
# login=denglu(pawd1=pawd2,user1=user2)
# print(login)  #打印才能显示返回值
#
# 函数里可以有默认参数，在不传参时，使用默认参数，如果传新值，使用新值
# def denglu(user1="longteng",pawd1="123456"):
#     user="longteng"
#     pawd="123456"
#     if(user1=="" or pawd1==""):
#         return "用户名或密码不能为空"
#     elif(user1==user and pawd1==pawd):
#         return "登录成功"
#     else:
#         return "用户名和密码不匹配"
#

# 求1--n的和
# def sum(x):
#     y=0
#     for i in range(1,x+1):
#         y=y+i
#     return y
# a=int(input("求1--n的和请输入数字："))
# b=sum(a)
# print(b)

# 导入包 见pack01 pack02


























