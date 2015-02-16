import random
#import shuffle
#a = ['hi','world','cat','dog']
#f=open('C:\Users\Subir\Desktop\student_ids_file','w')
#print f
#f.read()
List = open("C:\Users\Subir\Desktop\student_ids_file.txt").readlines()
#print a
random.shuffle(List,random=None)
#print a
f=open("C:\Users\Subir\Desktop\student_ids_file_new.txt",'w')
#len(List)

#for index1 in range(0,126):
#   List[index1].strip('\n')

List = map(lambda s: s.strip(), List)
print List    
group_no=1
#for index in range(0,120,4):
for index in range(len(List)):
    #if (len(List))
    var1=List[index]
    var2=List[index+1]
    var3=List[index+2]
    var4=List[index+3]
    var_disp='g-group'+str(group_no)+':'+var1+','+var2+','+var3+','+var4+';'
    group_no=group_no+1;
    f.write(var_disp)
    f.write('\n')    
f.close()
