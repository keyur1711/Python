def val(**a):
    lst=[]
    dic={}
    for i in a.values():
        lst.append(i)
    
    lst.reverse()
    
    
    for i in lst:
        for j in a.items():
            if j[1]==i:
                dic[j[0]]=j[1]
    print(dic)
val(key="1",key2="2",key4="4",key5="5",key3="3")