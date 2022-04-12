'''用户可以随意输入需要显示的行数。
（如输入13:21打印第13行到第21行，输入:21打印前21行
输入21:则打印从第21行开始到文件结尾所有内容）
'''

file_name=input("请输入要打开的文件：")  #测试文件为E:\Me\PYTHON\readme.txt,共15
lines=input("请输入需要显示的行数【格式如2:14或:8或3:】：")

#lines存放开始行和结束行构成的列表
lines=lines.split(':')

if lines[0]=='':
    l_start=0
else:
    l_start=int(lines[0])
    
if lines[1]=='':
    l_end=9999
else:
    l_end=int(lines[1])

f=open(file_name,'r',encoding='utf-8')

if l_start==0:
    if l_end==9999:
        print("文件",file_name,"的全文内容如下：")
    else:
        print("文件",file_name,"从开始到第",l_end,"行内容如下：")
else:
    if l_end==9999:
        print("文件",file_name,"从",l_start,"行到结尾内容如下：")
    else:
        print("文件",file_name,"从",l_start,"行到第",l_end,"行内容如下：")
count=0
for eachline in f:
    if (count>=l_start-1) and (count <=l_end-1):
        print(eachline)
    elif count>l_end-1:
        break
    count+=1

f.close()
    
    
