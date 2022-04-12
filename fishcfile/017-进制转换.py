#用除2取余法将十进制数-->二进制数

def transform(x):
    #商为b,余数为c
    s=[]
    b=x//2
    c=x%2
    #把每一个余数添加到列表中
    s.append(c)
    while b!=0:
        x=b
        b=x//2
        c=x%2
        s.append(c)
  #将列表元素倒转，就是二进制形式，出错
    result=''
    while s:
        result+=str(s.pop())
    return result
        
   
