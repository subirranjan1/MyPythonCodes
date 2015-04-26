import json
List = open("C:\Users\Subir\Desktop\student_ids_file.txt").readlines()
f=open("C:\Users\Subir\Desktop\stu.json",'w')
List = map(lambda s: s.strip(), List)
f.write("{")
f.write('\n')
for index in range(0,52):
    import json
    dic={'userid': List[index],"done": {"mark": '2.00', "comment": "Comment on Done."}}
    json=json.dumps(dic)
    f.write(json)
    f.write(',')
    f.write('\n')    

for index in range(53,125):
    import json
    dic={'userid': List[index],"done": {"mark": '0.0', "comment": "Comment on Done."}}
    json=json.dumps(dic)
    f.write(json)
    f.write(',')
    f.write('\n')    
f.close()
