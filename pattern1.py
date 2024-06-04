'''
for i in range(1,6):
    for j in range(1,6):
        print("*",end="")
    print()'''

'''
for i in range(5,0,-1):
    for j in range(5,0,-1):
        print(j,end="")
    print()'''

'''
for i in range(1,6):
    for j in range(1,6):
        if(i==j):
            print("$",end="")
        else:
            print("*",end="")
    print()'''
    
'''
for i in range(5,0,-1):
    for j in range(1,6):
        if(j==i):
            print("$",end="")
        else:
            print("*",end="")
    print()'''
'''    
for i in range(5,0,-1):
    for j in range(1,6):
        if(j==i):
            
            print("$",end="")
        else:
            if i==5 or i==1:
                print("*",end="")
            elif j==1 or j==5:
                print("*",end="")
            else:
                print(" ",end="")
           
    print()
'''

'''
for i in range(1,7):  
    for j in range(1,i):  
        print(j, end=' ')  
    print('') 
'''


for i in range (1,6):
    k=i;
    for j in range(i):
        print(k,end="")
        k+=1
    print()
    

'''
for i in range(6):
    for j in range(5,5-i,-1):
        print(j,end="")
    print()
'''

