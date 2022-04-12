#编写一个程序，接受用户的输入并保存为新的文件

file_name=input("请输入文件名：")
print("请输入内容【单独输入':w'保存退出】：")

#打开文件
f=open(file_name,'w')

#只要没遇到:w就一直往文件中写入
while True:
    write_some=input()
    if write_some !=':w':
        #换行打印
        f.write('%s\n' % write_some)
    else:
        break
f.close()

