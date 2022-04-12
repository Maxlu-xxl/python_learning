while 1:
    temp=input("请输入一个整数（输入Q结束程序):")
    if temp!='Q':
        num=int(temp)
        #使用内置函数输出
        print("十进制—>十六进制：",num,'->',hex(num))
        print("十进制—>八进制：",num,'->',oct(num))
        print("十进制—>十六进制：",num,'->',bin(num))
        #用print实现格式化
        print("十进制—>十六进制：%d -> 0x%x" %(num,num))
        print("十进制—>八进制：%d -> 0o%o" %(num,num))
    else:
        break
    


