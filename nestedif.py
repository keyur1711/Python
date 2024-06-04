a=int(input("Enter the first value"))
b=int(input("Enter the Second value"))
c=int(input("Enter the Third value"))

if(a>b):
    if(a>c):
        print("A is Max")
    elif(a==b and a==c):
        print("Equal")
    else:
        print("C is Max")
        
elif(a==b and a==c and b==a and b==c and c==a and c==b):
    print("Equal")
    
else:
    if(b>c):
        print("B is Max")
    else:
       print("C is Max")