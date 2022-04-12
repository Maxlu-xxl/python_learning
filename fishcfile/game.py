"""缩进对python很重要"""
import random
count=3
while count>0:
    temp=input("猜猜我想的是什么数字？")
    guess=int(temp)
    if guess==random.randint(1,10):
        print("猜对了")
        break
    else:
        if guess>8:
            print("大了")
        else:
            print("小了")
        count=count-1
        
print("游戏结束啦")
