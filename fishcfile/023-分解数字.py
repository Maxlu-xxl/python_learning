"写一个函数get_digits(n)，将参数n分解出每个位的数字并按顺序存放到列表中。"
"举例：get_digits(12345) ==> [1, 2, 3, 4, 5]"

result=[]

def get_digits(n):
    if n:
        result.insert(0,n%10)
        get_digits(n//10)
number=int(input("请输入数字："))
get_digits(number)
print(result)


    
