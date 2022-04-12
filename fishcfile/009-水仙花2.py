for i in range(100,1000):
    one=i//100
    two=(i-one*100)//10
    three=i-(i//10)*10
    if i==one**3+two**3+three**3:
        print(i)

    
