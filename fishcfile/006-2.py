#ladder=0
#while ladder<10000:
#    if ladder%2==1 and ladder%3==2 and ladder%5==4 and ladder%6==5 and ladder%7==0:
#        print("该阶梯至少有:",end='');print(ladder,end='');print("阶")
#        break
#    else :
#        ladder=ladder+1
#改进分析，因为可整除7，所以阶梯数为7的倍数，提高效率，避免从1开始加
ladder=7
i=1
while i<100:
    if ladder%2==1 and ladder%3==2 and ladder%5==4 and ladder%6==5:
        print("该阶梯数为",ladder)
        break
    else:
        ladder=7*(i+1)   #ladder以7的倍数地址
        i=i+1
if i >=100:
    print("在限定范围内找不到答案")




