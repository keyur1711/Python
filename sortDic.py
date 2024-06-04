dic={'val':1,'val2':5,'val3':3}
lst=[]
dic2={}
for i in dic.values():
    lst.append(i)
lst.sort()
print(dic.items())
for j in lst:
    for i in dic.items():
        if i[1]==j:
            dic2[i[0]]= j 
print(dic2)