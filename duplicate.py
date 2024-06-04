'''
lst=[5,5,2,5,4]

for i in range(len(lst)):
    for j in range(len(lst)):
        if(5==lst[j]):
            lst[j]=0
print(lst)'''

#for count duplicate values

lst=[5,5,2,5,4,5,5,5,5,5,5]
count=0
for i in range(len(lst)):
    if(5==lst[i]):
        count=count+1
print(count)
            