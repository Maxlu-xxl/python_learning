# 编写一个程序，当用户输入文件名和行数（N）后，将该文件的前N行内容打印到屏幕上
file_name=input("请输入要打开的文件：")
line=int(input("请输入需要显示该文件前几行："))
count=0

f=open(file_name,'r',encoding='utf-8')
print("文件",file_name,"的前",line,"的内容如下：")

for each_line in f:
    if count>=line:
        break
    count+=1
    print(each_line)

f.close()





    
