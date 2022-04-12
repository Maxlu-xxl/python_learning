#文件的读取和修改写入测试
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

if answer=='YES':
    f=open(filename,'r',encoding='utf-8')
    f_w=open("test_w.txt","w",encoding="utf-8")
    content=[]
    for eachline in f:
        if words in eachline: 
            eachline=eachline.replace(words,new_words)
        f_w.write(eachline)
    f_w.close()
    f.close()
        
