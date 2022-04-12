temp=input("请输入一个年份:")
while not temp.isdigit():    #s为字符串，s.isdigit()所有字符为数字。为真返true
    temp=input("输入有误，请输入一个整数：")
year=int(temp)
if year%4==0 and year%100!=0:
    print(temp+"是闰年")
else:
    if year%400==0:
        print(temp+"是闰年")
    else:
        print(temp+"不是闰年")
    
