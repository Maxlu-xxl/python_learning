#密码验证程序，用户只有三次机会输入错误，输入内容中包含*不减少次数
count=3  #用来表示三次输入机会
passward='xxllovely'
i=0
while count>0:
    temp=input("请输入密码：")
    if temp==passward:
        print("密码正确，进入程序.....")
        break
    else:
        if '*'in temp:
            print("密码中不能含有‘*’号！您还有3次机会",end=' ')
            count=3
        else:
            count-=1
            print("密码输入错误，您还有",count,"次机会",end=' ')
             
       
        
