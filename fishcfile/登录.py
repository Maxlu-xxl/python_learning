d={}
instruct=''
while (instruct!='q'or instruct!= 'Q'):
    print()
    print("|---新建用户：N/n---|")
    print("|---登陆账户：E/e---|")
    print("|---退出程序：Q/q---|")
    instruct=input("|---请输入指令代码：")
    if (instruct=='N'or instruct=='n'):
        name=input("请输入用户名：")
        if name in d:
            name=input("该用户名已被使用，请重新输入：")
        passwd=input("请输入密码：")
        d[name]=passwd
        print("注册成功，赶紧试试登陆吧")
    elif (instruct=='E'or instruct=='e'):
        name=input("请输入用户名：")
        if name not in d:
            name=input("您输入的用户名不存在，请重新输入：")
        passwd=input("请输入密码：")
        d[name]=passwd
        print("欢迎进入xxx系统，请输入Q/q退出程序")
    elif (instruct=='q'or instruct=='Q'):
        print("退出程序")
        break
            
