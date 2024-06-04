from class_database import mysqlconnect
import re
M = mysqlconnect()
class Seller():
    def reg(self):
        
        #global M
        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        try:
            self.email = input("Enter your Email:-")
            self.password = input("Enter your Password:-")
            if self.email==' ' or self.password==' ' or self.email=='' or self.password=='':
                raise ValueError("Please Enter All Fields...")
            
            if not re.match(email_pattern, self.email):
                raise ValueError("Please enter a valid email address like(abc@gmail.com)")
            
            
            Q_check = "SELECT * FROM seller WHERE email = %s"
            x = M.cursor()
            x.execute(Q_check, (self.email,))
            if x.fetchone():
                raise ValueError("Email already registered.")
            Q="insert into seller values('"+self.email+"','"+self.password+"');"
            print(Q)
            x = M.cursor()
            x.execute(Q)
            M.commit()
        except ValueError as ve:
            print(ve)
    
    def log(self):
        try:
            self.email = input("Enter your Registerd Email:-")
            self.password = input("Enter your Registerd Password:-")
            
            Q = "select * from seller where email='"+self.email+"' and password='"+self.password+"'"
            x = M.cursor()
            x.execute(Q)
            
            data = x.fetchall()
            print(data)
            login_successful = False
            
            for i in data:
                if i[0]==self.email and i[1]==self.password:
                    print("Login Successfully...")
                    login_successful = True
                    break
                    
            else:
                print("Invalid Email And Password")
            
            if login_successful:
                self.menu()
        except:
            print("Somthing Went Wrong...")
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
            try:
                print("1.Add Product:-")
                print("2.Remove Product:-")
                print("3.Update Product:-")
                print("4.Display Product:-")
                print("0. Exit")
                
                a= int(input("Enter Your Choice:-"))
                z=Questionlab(a)
                if z==0:
                    break
            except ValueError:
                print("Please Enter Only Number Between 0 to 4")