# 登录函数
def denglu(user1,pawd1):
    user="longteng"
    pawd="123456"
    if(user1=="" or pawd1==""):
        return "用户名或密码不能为空"
    elif(user1==user and pawd1==pawd):
        return "登录成功"
    else:
        return "用户名和密码不匹配"
# 求1--n的和
def sum1(x):
    y=0
    for i in range(1,x+1):
        y=y+i
    return y

# 调试代码用，不会在别的模块引用
if __name__ == '__main__':
    user2 = input("请输入用户名：").strip()
    pawd2 = input("请输入密码：").strip()
    login = denglu(user2, pawd2)
    print(login)  # 打印才能显示返回值



