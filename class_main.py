from class_seller import Seller
from class_buyer import Buyer
from class_database import mysqlconnect



while True:
    try:
        print("1. Seller ")
        print("2. Buyer ")
        print("0. Exit ")
        
        a=int(input("Enter Your Choice:-"))
        
        if a==1:
            s = Seller()
            
            while True:
                try:
                    print("1. Register")
                    print("2. Login")
                    print("0. Exit")
                    Sr=int(input("Enter your Choice:-"))
                    
                    if Sr==1:
                        s.reg()
                    elif Sr==2:
                        s.log()
                        
                    elif Sr==0:
                        print("Exit")
                        break
                    else:
                        print("Invalid Choice..")
                except ValueError:
                    print("Please Enter Only Number Between 0 to 2")
        elif a==2:
            b = Buyer()
            
            while True:
                try:
                    print("1. Register")
                    print("2. Login")
                    print("0. Exit")
                    
                    Br=int(input("Enter Your Choice:-"))
                    
                    if Br==1:
                        b.reg()
                    elif Br==2:
                        b.log()
                        
                    elif Br==0:
                        print("Exit")
                        break
                    else:
                        print("Invalid Choice..")
                except ValueError:
                    print("Please Enter Only Number Between 0 to 2")
        elif a==0:
            print("Bay Bay...")
            break
        else:
            print("Invalid Choice")
    except ValueError:
        print("Please Enter Only Number Between 0 to 2")