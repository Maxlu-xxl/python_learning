'''编写一个程序，实现“全部替换”功能'''
#思考：为什么要打开两次文件呢？怀疑可能第一次打开文件计数后文件自动关闭了
filename=input("请输入文件名：")
words=input("请输入需要替换的字符或单词：")
new_words=input("请输入新的单词或字符：")

f=open(filename,'r',encoding='utf-8')
count=0
for eachline in f:
    count+=eachline.count(words)  
print("文件",filename,"中共有",count,"个【",words,"】")
f.close()

print("您确定把所有的【",words,"】替换为【",new_words,"】吗？")
answer=input("【YES/NO】：")
'''
#法一：
if answer=='YES':
    f=open(filename,'r',encoding='utf-8')
    f_w=open("f_w.txt","w",encoding="utf-8")
    content=[]
    for eachline in f:
        if words in eachline: 
            eachline=eachline.replace(words,new_words)
        content.append(eachline)
    f_w.writelines(content)
    f_w.close()
    f.close()
'''
#法二
if answer=='YES':
    f=open(filename,'r',encoding='utf-8')
    f_w=open("f_w.txt","w",encoding="utf-8")
    for eachline in f:
        if words in eachline: 
            eachline=eachline.replace(words,new_words)
        f_w.write(eachline)
    f_w.close()
    f.close()
    
        

