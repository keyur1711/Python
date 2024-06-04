from class_database import mysqlconnect
import re
M = mysqlconnect()
addcart=[]
class Buyer():
    def reg(self):
        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        try:
            
            self.email = input("Enter your Email:-")
            self.password = input("Enter your Password:-")
            if self.email == ' ' or self.password ==" " or self.email == '' or self.password =="":
                raise ValueError("Please Enter All Fields..")
            
            if not re.match(email_pattern, self.email):
                raise ValueError("Please enter a valid email address like(abc@gmail.com)")
            
            
            Q_check = "SELECT * FROM buyer WHERE email = %s"
            x = M.cursor()
            x.execute(Q_check, (self.email,))
            if x.fetchone():
                raise ValueError("Email already registered.")
                
            Q="insert into buyer values('"+self.email+"','"+self.password+"');"
            
            x = M.cursor()
            x.execute(Q)
            M.commit()
            
        except ValueError as ve:
            print(ve)
    def log(self):
        try:
            Q="select * from buyer"
            x = M.cursor()
            x.execute(Q)
            
            data = x.fetchall()
            print(data)
            
            self.email=input("Enter Your Reisterd Email:-")
            self.password=input("Enter Your Reisterd Password:-")
            
            login_successful = False
            
            for i in data:
                if i[0]==self.email or i[1]==self.password:
                    print("Login Successfully...")
                    login_successful = True
                    break
            else:
                print("Invalid Email And Password...")
            if login_successful:
                self.buyer_menu()
        except:
            print("Somthing Went Wrong..")
    def dispro(self):
        try:
            Q="select * from product"
            x=M.cursor()
            x.execute(Q)
            
            data = x.fetchall()
            print(data)
            
            for i in data:
                print("Product Name:-",i[1])
                print("Product Category:-",i[2])
                print("Product Price:-",i[3])
                print("Product Quantity:-",i[4])
                print("Product Description:-",i[5])
                print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
        
        except:
            print("Somthing Went Wrong...")
            
    
               
            
    def serpro(self):
        try:
            serchName=input("Enter Product Name To Be Serched:-")
            
            Q="select * from product where proName='"+serchName+"'"
            x=M.cursor()
            x.execute(Q)
            
            data= x.fetchall()
            print(data)
            for i in data:
                print("Product Name:-",i[1])
                print("Product Category:-",i[2])
                print("Product Price:-",i[3])
                print("Product Quantity:-",i[4])
                print("Product Description:-",i[5])
                print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
        except:
            print("Somthing Went Wrong...")
    def serprocat(self):
        try:
            serchName=input("Enter Product Category To Be Serched:-")
            
            Q="select * from product where proCategory='"+serchName+"'"
            x=M.cursor()
            x.execute(Q)
            
            data= x.fetchall()
            print(data)
            for i in data:
                print("Product Name:-",i[1])
                print("Product Category:-",i[2])
                print("Product Price:-",i[3])
                print("Product Quantity:-",i[4])
                print("Product Description:-",i[5])
                print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
        except:
            print("Somthing Went Wrong...")
    def priceh(self):
        try:
            Q="select * from product"
            x=M.cursor()
            x.execute(Q)
            
            data=x.fetchall()
            print(data)
            pricelst=[]
            for i in data:
                pricelst.append(i[3])
                
            pricelst.sort(reverse=True)
                
              
            for i in pricelst:
                for j in data:
                    if j[3] == i:
                        print("Product Name:-",j[1])
                        print("Product Category:-",j[2])
                        print("Product Price:-",j[3])
                        print("Product Quantity:-",j[4])
                        print("Product Description:-",j[5])
                        print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
        except:
            print("Somthing Went Wrong...")
    def pricel(self):
        try:
            Q="select * from product"
            x=M.cursor()
            x.execute(Q)
            
            data=x.fetchall()
            print(data)
            pricelst=[]
            for i in data:
                pricelst.append(i[3])
                
            pricelst.sort()   
               
            for i in pricelst:
                for j in data:
                    if j[3] == i:
                        print("Product Name:-",j[1])
                        print("Product Category:-",j[2])
                        print("Product Price:-",j[3])
                        print("Product Quantity:-",j[4])
                        print("Product Description:-",j[5])
                        print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
        except:
            print("Somthing Went Wrong...")
    def addcart(self):
        try:
            print("Current cart contents:")
            grand_total = 0
            for item in addcart:
                product, quantity = item
                total_price = product[3] * quantity
                grand_total += total_price
                print("Product Name:", product[1])
                print("Product Category:", product[2])
                print("Product Price:", product[3])
                print("Product Quantity Bought:", quantity)
                print("Product Description:", product[5])
                print("Total Price for this product:", total_price)
                print("========================================")
            print("Grand Total of All Products:", grand_total)
        except:
            print("Somthing Went Wrong...")
            
    def buyer_menu(self):
        
        while True:
            try:
                print("1. Display All Products")
                print("2. Search Product By Name")
                print("3. Search Product By Category")
                print("4. Price High To Low")
                print("5. Price Low To High")
                print("6. Add To Cart")
                print("0. Exit")
                
                choice = int(input("Enter Your Choice: "))
                
                if choice == 1:
                    self.dispro()
                    self.pro_qun()
                elif choice == 2:
                    self.serpro()
                    self.pro_qun()
                elif choice == 3:
                    self.serprocat()
                    self.pro_qun()
                elif choice == 4:
                    self.priceh()
                    self.pro_qun()
                elif choice == 5:
                    self.pricel()
                    self.pro_qun()
                elif choice == 6:
                    self.addcart()
                elif choice == 0:
                    print("Exit...")
                    break
                else:
                    print("Invalid Choice.")
            except ValueError:
                print("Please Enter Only Number Between 0 to 6")
    def pro_qun(self):
        try:
            Q="select * from product"
            x=M.cursor()
            x.execute(Q)
            
            data = x.fetchall()
            print(data)
            data = [list(row) for row in data]
            
            buy_choice = input("Do you Want Any Product (y/n): ")
            
            if buy_choice in ['y', 'yes']:
                pro_name = input("Enter Product Name To Be Bought: ")
                
                for product in data:
                    if product[1] == pro_name:
                        quantity_to_buy = int(input("Enter Quantity to Buy: "))
                        
                        if quantity_to_buy <= product[4]:
                            confirm_buy = input("Are You Confirm To Buy This Product? (y/n): ")
                            
                            if confirm_buy in ['y', 'yes']:
                                
                                addcart.append((product,quantity_to_buy))
                                print("Product added to cart.")
                                
                                new_quantity =product[4] - quantity_to_buy
                                
                                Q="update product set proQuntity='"+str(new_quantity)+"' where proName='"+pro_name+"'"
                                x=M.cursor()
                                x.execute(Q)
                                M.commit()
                               
                                product[4] = new_quantity
                                print("Quantity Updated In DataBase")
                            else:
                                print("Purchase Canceled.")
                        else:
                            print("Sorry, Not Enough Quantity Available.")
                        break
                else:
                    print("Product Not Found.")
        except:
            print("Somthing Went Wrong...")