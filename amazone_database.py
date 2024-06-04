import mysql.connector as mc

M = mc.connect(host="localhost",user="root",password="1711",database="amazone")

class Seller():
    global M
    def reg(self):
        
        
        self.email = input("Enter your Email:-")
        self.password = input("Enter your Password:-")
           
        Q="insert into seller values('"+self.email+"','"+self.password+"');"
        print(Q)
        x = M.cursor()
        x.execute(Q)
        M.commit()
    
    def log(self):
        Q = "select * from seller"
        x = M.cursor()
        x.execute(Q)
        
        data = x.fetchall()
        print(data)
        
        self.email = input("Enter your Registerd Email:-")
        self.password = input("Enter your Registerd Password:-")
        
        for i in data:
            if i[0]==self.email:
                print("Login Successfully...")
                break
        else:
            print("Invalid Email And Password...")
    def menu(self):
        def Questionlab(a):
        
            if a==1:
                name=input("Enter Product Name:-")
                category=input("Enter Product Category:-")
                price=int(input("Enter Product Price:-"))
                totalQ=int(input("Enter Product Quantity:-"))
                description=input("Enter Product Description:-")
                
                Q="insert into product(proName, proCategory, proPrice, proQuntity, proDesc) values ('"+name+"','"+category+"','"+str(price)+"','"+str(totalQ)+"','"+description+"')"
                x = M.cursor()
                x.execute(Q)
                M.commit()
            elif a==2:
                delpro=input("Enter The Product Name To Be Deleted:-")
                
                Q="select * from product where proName='"+delpro+"'"
                x=M.cursor()
                x.execute(Q)
                
                
                data = x.fetchall()
                print(data)
                
                if data[0][1]==delpro:
                    Q="delete from product where ProName='"+delpro+"'"
                    x = M.cursor()             
                    x.execute(Q)
                    M.commit()
            elif a==3:
                upro=input("Enter Your Product Name To Be Updated:-")
                
                Q="select * from product where proName='"+upro+"'"
                x=M.cursor()
                x.execute(Q)
                
                
                data = x.fetchall()
                print(data)
                if data[0][1]==upro:
                    uproname=input("Enter New Product Name:-")
                    uprocategory=input("Enter New product Category:-")
                    uproprice=int(input("Enter New Product Price:-"))
                    uprototalQ=int(input("Enter New Product Quantity:-"))
                    uprodesc=input("Enter New Product Description:-")
                    
                    Q="update product set proName='"+uproname+"', proCategory='"+uprocategory+"', proPrice='"+str(uproprice)+"', proQuntity='"+str(uprototalQ)+"', proDesc='"+uprodesc+"' where proName='"+upro+"'"
                    x=M.cursor()
                    x.execute(Q)
                    M.commit()
            elif a==4:
                Q="select * from product"
                x = M.cursor()
                x.execute(Q)
                
                data=x.fetchall()
                print(data)
                for i in data:
                    print("product Name:-",i[1])
                    print("product Category:-",i[2])
                    print("product Price:-",i[3])
                    print("product Quantity:-",i[4])
                    print("product Description:-",i[5])
                    print("-*-*-*-*-*-*-*-*-*-*")
            elif a==0:
                print("Exit")
                return 0
            else:
                print("Invalid Choice..")
                
                    
        while True:
            print("1.Add Product:-")
            print("2.Remove Product:-")
            print("3.Update Product:-")
            print("4.Display Product:-")
            print("0. Exit")
            
            a= int(input("Enter Your Choice:-"))
            z=Questionlab(a)
            if z==0:
                break
class Buyer():
    def reg(self):
        self.email = input("Enter your Email:-")
        self.password = input("Enter your Password:-")
           
        Q="insert into buyer values('"+self.email+"','"+self.password+"');"
        print(Q)
        x = M.cursor()
        x.execute(Q)
        M.commit()
    def log(self):
        Q="select * from buyer"
        x = M.cursor()
        x.execute(Q)
        
        data = x.fetchall()
        print(data)
        
        self.email=input("Enter Your Reisterd Email:-")
        self.password=input("Enter Your Reisterd Password:-")
        
        for i in data:
            if i[0]==self.email or i[1]==self.password:
                print("Login Successfully...")
                break
            else:
                print("Invalid Email And Password...")
while True:
    print("1. Seller ")
    print("2. Buyer ")
    print("0. Exit ")
    
    a=int(input("Enter Your Choice:-"))
    
    if a==1:
        s = Seller()
        
        while True:
            print("1. Register")
            print("2. Login")
            print("0. Exit")
            Sr=int(input("Enter your Choice:-"))
            
            if Sr==1:
                s.reg()
            elif Sr==2:
                s.log()
                s.menu()
            elif Sr==0:
                print("Exit")
                break
            else:
                print("Invalid Choice..")
    elif a==2:
        b = Buyer()
        
        while True:
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