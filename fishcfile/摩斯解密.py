#摩斯密文表
c_table=[".-","-...","-.-.","-..",".","..-.",
         "--.","....","..",".---","-.-",".-..",
         "--","-.","---",".--.","--.-",".-.",
         "...","-","..-","...-",".--","-..-",
         "-.--","--..",".----","..---","...--","....-",
         ".....","-....","--...","---..","----.","-----"]

#摩斯明文表
d_table=["A","B","C","D","E","F",
         "G","H","I","J","K","L",
         "M","N","O","P","Q","R",
         "S","T","U","V","W","X",
         "Y","Z","1","2","3","4",
         "5","6","7","8","9","0"]
code=input("请输入摩斯密码:")
#按空格划分输入的字符串
split_code=code.split(" ")

#result=[d_table[c_table.index(each)] for each in split_code]
result=[]
for each in split_code:
    i=c_table.index(each)   #找到each在c_table列表中的索引
    result.append(d_table[i])  #根据索引找到d_table中的元素加入result列表中
print(result)
