user_data={}


def new_user():
    name=input("请输入用户名：")
    #需要一个循环，仅当输入用户名未注册过才可输入密码
    while name in user_data:
        name=input("该用户名已经被使用，请重新输入：")
    passwd=input("请输入密码:")
    user_data[name]=passwd
    print("注册成功，赶紧试试登陆吧")

def old_user():
    name=input("请输入用户名：")
    #需要一个循环，仅当输入的用户名已注册过才可登录
    while name not in user_data:
        name=input("你输入的用户名不存在，请重新输入：")
    passwd=input("请输入密码：")
    #需要验证登录密码是否正确
    password=user_data.get(name)
    if passwd==password:
        print("欢迎进入xxx系统，可以输入q/Q退出程序")
    else:
        print("密码错误")


def showmenu():
    while 1:
        
        prompt = '''
|--- 新建用户：N/n ---|
|--- 登录账号：E/e ---|
|--- 推出程序：Q/q ---|
|--- 请输入指令代码：'''
        choice=input(prompt)
        if (choice=="N")or (choice=="n"):
            new_user()
        elif (choice=="E")or (choice=="e"):
            old_user()
        elif (choice=="Q")or (choice=="q"):
            break
        else:
            print("请输入正确的指令代码")
    

#调用showmenu()函数
showmenu()
