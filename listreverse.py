lst=[19,39,49,18,7,17,45]

for i in range(len(lst)):
    for j in range(len(lst)-1):
        if(lst[j]<lst[j+1]):
            c=lst[j+1]
            lst[j+1]=lst[j]
            lst[j]=c
print(lst)