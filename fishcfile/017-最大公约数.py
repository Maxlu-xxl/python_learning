#欧几里得算法求最大公约数

def gcd(x,y):
    #商为b,余数为c
    b=x//y
    c=x%y
    while c!=0:
        x=y
        y=c
        b=x//y
        c=x%y
    return y
        
    
