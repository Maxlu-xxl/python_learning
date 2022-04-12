temp = input('请输入一个整数:')
number = int(temp)
while number:
    i = number - 1
    while i:   #打印*前的空格
        print(' ',end='')   #print默认输出是换行的，如果不想换行
        i = i - 1              #需要在变量末尾加上逗号，end='',表示该行不换行
    j = number
    while j:  #打印*号
        print('*', end = '')
        j = j - 1
    print()  #实现换行
    number = number - 1  #打印行数为输入整数
