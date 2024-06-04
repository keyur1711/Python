dic={'val':1,'val2':5,'val3':3}
lst=[]
dic2={}
for i in dic.values():
    lst.append(i)
print(lst) 
lst.reverse()
print(lst)

for i in lst:
    for j in dic.items():
       if j[1]==i:
            dic2[j[0]]=j[1]
print(dic2)