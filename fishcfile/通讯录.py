print("|---欢迎进入通讯录程序---|")
print("|---1:查询联系人资料  ---|")
print("|---2:插入新的联系人  ---|")
print("|---3:删除已有联系人  ---|")
print("|---4:退出通讯录程序  ---|")
num=0
d={"小甲鱼":"020-88974651","陆丽芳":"010-12345678"}
while num!=4:
    print()
    temp=input("请输入相关指令代码：")
    num=int(temp)
    if num==1:
        name=input("请输入联系人姓名：")
        if name in d:
            print(name,"：",d[name])
        else:
            print("该联系人不在通讯录中")
    elif num==2:
        name=input("请输入联系人姓名：")
        if name in d:
            print("你输入的姓名在通讯录中已存在-->>",name,":",d[name])
            answer=input("是否修改用户资料(YES/NO):")
            if answer=='YES':
                tel=input("请输入用户联系电话：")
                d[name]=tel
                print(d)
            else:
                break
        else:   
            tel=input("请输入用户联系电话：")
            d.setdefault(name,tel)
    elif num==3:
        name=input("请输入联系人姓名：")
        if name in d:
            del d[name]
        else:
            print("您要删除的联系人不在通讯录中")
    elif num==4:
        print("|---感谢使用通讯录程序---|")
    
    

    
    
