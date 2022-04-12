def count(*param):
    "统计传入字符串参数（可能不止一个参数）的英文字母、空格、数字和其他字符"
    length=len(param)
    '''
    chars="abcdefghijklmnopqrstuvwxyz"
    nums="0123456789"'''
    for each_str_index in range(length):
        c,n,space,others=0,0,0,0
        for each in param[each_str_index]:
            if each.isalpha():
                c+=1
            elif each.isdigit():
                n+=1
            elif each == ' ':
                space+=1
            else:
                others+=1
        print("第",each_str_index+1,"个字符共有：英文字母",c,"个，数字",n,"个，空格",space,"个，其他字符",others,"个")

    
