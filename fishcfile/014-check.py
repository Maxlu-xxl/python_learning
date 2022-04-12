"""写的还是有点小问题，初级密码要么全部是数字或者字母组成，中级则是数字、字母、特殊字符任意两个
"""
symbols = r'''`!@#$%^&*()_+-=/*{}[]\|'";:/?,.<>'''
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
nums = '0123456789'
password=input("请输入密码")
length=len(password)
flat=0
n,c,s=0,0,0
if length<=8:
    flat==1
elif length>8 and length<16:
    flat=2
elif length>=16:
    flat=3
for each in password:
    if each in nums:
        n+=1
    elif each in chars:
        c+=1
    elif each in symbols:
        s+=1
if n+c+s==length:
    if flat==1 and (n or c) and (s==0):
        print("密码等级位初级")
    elif flat==2 and n and (c or s):
        print("密码等级位中级")
    elif flat==3 and n and c and s:
        print("密码等级为高级")
    else:
        print("密码不合要求")
    
    
    
