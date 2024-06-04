dic={}
while True:
    print("1. Add ")
    print("2. Display ")
    print("3. Delete ")
    print("4. Update ")
    
    a=int(input("Enter Your Choice:-"))
    
    if a==1:
        key=input("Enter Key To Be Add")
        value=int(input("Enter Value To Be Add"))
        if key in dic:
            print("Not Possible")
        else:
            dic[key]=value
    elif a==2:
        print(dic)
    elif a==3:
        key=input("Enter key to delete")
        if key in dic:
            dic.pop(key)
        else:
            print("Not Avilable Key")
    elif a==4:
        key=input("Enter Key To Be Update Value")
        if key in dic:
            Newvalue=int(input("Enter The New Value"))
            dic[key]=Newvalue
        else:
            print("Please Enter Valid Key")
    else:
        print("Invalid Choice")
    print(dic)