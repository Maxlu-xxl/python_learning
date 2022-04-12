

def save_file(girl,boy,count):
    file_name_girl='girl_'+str(count)+'.txt'
    file_name_boy='boy_'+str(count)+'.txt'
        
    boy_file=open(file_name_boy,'w',encoding='utf-8')
    girl_file=open(file_name_girl,'w',encoding='utf-8')

    girl_file.writelines(girl)
    boy_file.writelines(boy)

    girl_file.close()
    boy_file.close()

def split_file(filename):
    girl=[]
    boy=[]
    count=1
    
    f=open(filename,'r',encoding='utf-8')

    for eachline in f:
        if eachline[:6]!='======':
            (role,spoken)=eachline.split('：',1)
            if role=='小小陆':
               girl.append(spoken)
            if role=='小小陈':
                boy.append(spoken)
        else:
            save_file(girl,boy,count)
            boy=[]
            girl=[]
            count+=1

    save_file(girl,boy,count)        
    f.close()

#调用
split_file('record.txt')

 
