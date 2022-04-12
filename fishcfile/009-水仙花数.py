#for i in range(100, 1000):
#    sum = 0
#    temp = i
#    while temp:
#        sum = sum + (temp%10) ** 3
#        temp //= 10         # 注意这里要使用地板除哦~
#    if sum == i:
#        print(i)

for number in range(100,1000):
    one=number//100
    two=(number-one*100)//10
    three=number-(number//10)*10
    if number==one**3+two**3+three**3:
    	print(number,"是水仙花数"number)
    else:
        number+=1

