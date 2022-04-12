"编写一个程序，比较用户输入的两个文件，如果不同，显示出所有不同处的行号与第一个不同字符的位置"

file_name_1=input("请输入需要比较的第一个文件名：")
file_name_2=input("请输入需要比较的第二个文件名：")

f1=open(file_name_1,'r',encoding='utf-8')
f2=open(file_name_2,'r',encoding='utf-8')

#分别按行读取每个文件并且进行比较

count=0 #用来记录不同之处
differ=[]

for line1 in f1:
    #print("我是file1:",line1)
    line2=f2.readline()
    #print("我是file2:",line2)
    count+=1
    if line1!=line2:
        differ.append(count)

#这样不行，为什么一个可以用line1,一个要用f2.readline()
'''
for line1 in f1:
    print(line1)
    for line2 in f2:
        print(line2)
        count+=1
        if line1!=line2:
            differ.append(count)
'''

f1.close()
f2.close()

if len(differ) == 0:
    print('两个文件完全一样！')
else:
    print('两个文件共有【%d】处不同：' % len(differ))
    for each in differ:
        print('第 %d 行不一样' % each)
            
    
