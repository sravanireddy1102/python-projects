f=open("internship.txt",'r',encoding='UTF-8')

count=0
for line in f.readlines():
    count+=len(line.split())
f.close()
print(count)