lst = []
while True:
    print("1. Add")
    print("2. Remove")
    print("3. update")
    print("4. Exit")
    print("5. Max Value from the List")
    print("6. Desending Order List")
    print("7. Duplicate Value from the List")
    print("8 .Count Duplicate Value")
    a = int(input("Enter your choice: "))
    if a == 1:
        app = int(input("Enter the value to add: "))
        lst.append(app)
    elif a == 2:
        rmv = int(input("Enter the value to remove: "))
        if rmv in lst:
        
            lst.remove(rmv)
        else:
            print("Invalid Remove Items")
    elif a == 3:
        
        upd = int(input("Enter the old value from the list"))  
        if upd in lst:
            ind=lst.index(upd)
            upd1= int(input("Enter the new value"))
            lst[ind]=upd1
        else:
            print("Invalid Old Value")
    elif a == 4:
        print("Exit")
        break
    elif a==5:
        max=0
        for i in lst:
            if i >max:
                max = i
        print(max)
    elif a==6:
        for i in range(len(lst)):
            for j in range(len(lst)-1):
                if(lst[j]<lst[j+1]):
                    c=lst[j+1]
                    lst[j+1]=lst[j]
                    lst[j]=c
        print(lst)
    elif a==7:
        user=int(input("Please Enter The value to Check Duplicate"))
        if user in lst:        
            for i in range(len(lst)):
                for j in range(len(lst)):
                    if(user==lst[j]):
                        lst[j]=0
            print(lst)
        else:
            print("Not Found")
    elif a==8:
        user=int(input("Please Enter The value to Check Duplicate"))
        
        count=0
        for i in range(len(lst)):
            if(user==lst[i]):
                count=count+1
        print(count)
    else:
        print("Invalid choice")
        break
    print(lst)
