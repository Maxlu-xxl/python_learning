def findstr():
    "编写一个函数 findstr()，该函数统计一个长度为 2 "
    "的子字符串在另一个字符串中出现的次数"
    str=input("请输入目标字符串：")
    str_son=input("请输入子字符串（两个字符）：")
    count=0
    if str_son in str:
        print("子字符串在目标字符串中")
    else:
        print("子字符串不在目标字符串中")
    #这里没有用for each in str :因为这样打印出来的是一个个字符，因此我们用str的长度获得下标进行比较
    for each in range(len(str)-1):
        if (str[each]==str_son[0]):
            if (str[each+1]==str_son[1]): 
                count+=1
    print("子字符串在目标字符串中共出现",count,"次")
    
