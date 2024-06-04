dic={'val':1,'val2':5,'val3':3,'val4':5}
lst=[]
dic2={}

for i in dic.values():
    lst.append(i)
print(lst)  

for i in lst:
    
    if lst.count(5)>1:
        lst.remove(5)           

for i in lst:
    for j in dic.items():
        if i not in dic2.values():
            if i == j[1]:
                dic2[j[0]]=j[1]
print(dic2)