def amazone():
    lst=[]
    counter=0
    productlst=[]
    addcart=[]

    while True:
        print("1. Admin")
        print("2. Buyer")
        print("0. Exit")
        
        a= int(input("Enter Your Choice:-"))
        
        if a==1:
            dic={}
            print("1. Register")
            print("2. Login")
            
            admin=int(input("Enter Your Choice:-"))
            
            if admin==1:
                email=input("Enter Email:-")
                password=input("Enter Password:-")
                
                dic['email']=email
                dic['password']=password
                
                lst.append(dic)
            elif admin==2:
                email=input("Enter Your Registerd Email:-")
                password=input("Enter Your Registerd Password:-")
                f=0
                for i in lst:
                    if i['email']==email:
                        f=1;
                        print("Login Successfully....")
                        
                        while True:
                            print("1. Add Product")
                            print("2. Remove Product")
                            print("3. Update Product")
                            print("4. Display Product")
                            print("0. Exit")
                            
                            pro=int(input("Enter Your Choice:-"))
                            
                            if pro==1:
                                name=input("Enter Product Name:-")
                                category=input("Enter Product Category:-")
                                price=int(input("Enter Product Price:-"))
                                totalQ=int(input("Enter Product Quantity:-"))
                                description=input("Enter Product Description:-")
                                
                                product={}
                                
                                product['name']=name
                                product['category']=category
                                product['price']=price
                                product['Quantity']=totalQ
                                product['description']=description
                                product['id']=counter
                                counter +=1
                                
                                productlst.append(product)
                            
                            elif pro==2:
                                delid=int(input("Enter The Product Id To Be Deleted:-"))
                            
                                for i in productlst:
                                    if i['id']==delid:
                                        productlst.pop(delid)
                            elif pro==3:
                                upro=int(input("Enter Your Product id To Be Updated:-"))
                                
                                for i in productlst:
                                    if i['id']==upro:
                                        uproname=input("Enter New Product Name:-")
                                        uprocategory=input("Enter New product Category:-")
                                        uproprice=input("Enter New Product Price:-")
                                        uprototalQ=input("Enter New Product Quantity:-")
                                        uprodesc=input("Enter New Product Description")
                                        
                                        product['name']=uproname
                                        product['category']=uprocategory
                                        product['price']=uproprice
                                        product['Quantity']=uprototalQ
                                        product['description']=uprodesc
                                
                            elif pro==4:
                                print(productlst)
                            elif pro==0:
                                print("Exit...")
                                break
                            else:
                                print("Invalid Choice...")
                                
                if f==0:
                    print("Invalid Login Details...")
                    
        elif a==2:
            dic={}
            print("1. Register")
            print("2. Login")
            
            admin=int(input("Enter Your Choice:-"))
            
            if admin==1:
                email=input("Enter Email:-")
                password=input("Enter Password:-")
                
                dic['email']=email
                dic['password']=password
                
                lst.append(dic)
            elif admin==2:
                email=input("Enter Your Registerd Email:-")
                password=input("Enter Your Registerd Password:-")
                f=0
                for i in lst:
                    if i['email']==email:
                        f=1;
                        print("Login Successfully....")
                        
                        while True:
                            print("1. Display All Product:-")
                            print("2. Search Product By Name:-")
                            print("3. Search Product By Category:-")
                            print("4. Price High To Low:-")
                            print("5. Price Low To High:-")
                            print("6. Add To Cart:-")
                            print("7. Support:-")
                            print("0. Exit:-")
                            
                            Buypro=int(input("Enter Your Choice:-"))
                            
                            if Buypro==1:
                                for product in productlst:
                                    print("Product:", product['name'])
                                    print("Category:", product['category'])
                                    print("Price:", product['price'])
                                    print("Quantity:", product['Quantity'])
                                    print("Description:", product['description'])
                                    print("==========================")
                                                                
                                buy_choice = input("Do you Want Any Product (y/n): ")
                                
                                if buy_choice in ['y', 'yes']:
                                    pro_name = input("Enter Product Name To Be Bought: ")
                                    
                                    for product in productlst:
                                        if product['name'] == pro_name:
                                            quantity_to_buy = int(input("Enter Quantity to Buy: "))
                                            
                                            if quantity_to_buy <= product['Quantity']:
                                                confirm_buy = input("Are You Confirm To Buy This Product? (y/n): ")
                                                
                                                if confirm_buy in ['y', 'yes']:
                                                    
                                                    addcart.append(product)
                                                    print("Product added to cart.")
                                                    
                                                    product['Quantity'] -= quantity_to_buy
                                                else:
                                                    print("Purchase Canceled.")
                                            else:
                                                print("Sorry, Not Enough Quantity Available.")
                                            break
                                    else:
                                        print("Product Not Found.")

                            
                            elif Buypro==2:
                                searchName = input("Enter Product Name To Be Searched: ")

                                found_product = None
                                for i in productlst:
                                    if searchName in i['name']:
                                        found_product = i
                                        break

                                if found_product:
                                    print("Product Found:")
                                    print("Name:", found_product['name'])
                                    print("Category:", found_product['category'])
                                    print("Price:", found_product['price'])
                                    print("Quantity:", found_product['Quantity'])
                                    print("Description:", found_product['description'])
                                    print("==========================")

                                    buy_product = input("Do You Want To Buy This Product? (y/n): ")
                                    if buy_product in ['y', 'yes']:
                                        quantity_to_buy = int(input("How Many Quantity do you Want? "))
                                        if quantity_to_buy <= found_product['Quantity']:
                                            confirm_buy = input("Are You Confirm To Buy This Product? (y/n): ")
                                            if confirm_buy in ['y', 'yes']:
                                                print("Confirmed...")
                                                found_product['Quantity'] -= quantity_to_buy
                                            else:
                                                print("Purchase Canceled.")
                                        else:
                                            print("Quantity is !")
                                    else:
                                        print("Cancle...")
                                else:
                                    print("Product Not Found.")
                            
                            elif Buypro==3:
                                searchCategory = input("Enter Category Name To Be Searched: ")
                                found_products = []

                                for product in productlst:
                                    if searchCategory.lower() in product['category']:
                                        found_products.append(product)

                                if found_products:
                                    print("Products Found:")
                                    for found_product in found_products:
                                        print("Name:", found_product['name'])
                                        print("Category:", found_product['category'])
                                        print("Price:", found_product['price'])
                                        print("Quantity:", found_product['Quantity'])
                                        print("Description:", found_product['description'])
                                        print("==========================")

                                    buy_product = input("Do You Want To Buy Any of These Products? (y/n): ")
                                    if buy_product in ['y', 'yes']:
                                        product_to_buy = input("Enter the Name of the Product You Want to Buy: ")
                                        for product in found_products:
                                            if product['name'].lower() == product_to_buy:
                                                quantity_to_buy = int(input("How Many Quantity do you Want? "))
                                                if quantity_to_buy <= product['Quantity']:
                                                    confirm_buy = input("Are You Confirm To Buy This Product? (y/n): ")
                                                    if confirm_buy in ['y', 'yes']:
                                                        print("Confirmed...")
                                                        product['Quantity'] -= quantity_to_buy
                                                        break
                                                    else:
                                                        print("Purchase Canceled.")
                                                else:
                                                    print("Sorry, Not Enough Quantity Available.")
                                        else:
                                            print("Product Not Found.")
                                else:
                                    print("No Products Found in this Category.")

                                            
                            elif Buypro==4:
                                
                                pricelst=[]
                                
                                for i in productlst:
                                    pricelst.append(i['price'])
                                    
                                    pricelst.sort(reverse=True)
                                    
                                print(pricelst)
                                
                                buy_choice = input("Do you Want Any Product (y/n): ")
                                
                                if buy_choice in ['y', 'yes']:
                                    pro_name = input("Enter Product Name To Be Bought: ")
                                    
                                    for product in productlst:
                                        if product['name'] == pro_name:
                                            quantity_to_buy = int(input("Enter Quantity to Buy: "))
                                            
                                            if quantity_to_buy <= product['Quantity']:
                                                confirm_buy = input("Are You Confirm To Buy This Product? (y/n): ")
                                                
                                                if confirm_buy in ['y', 'yes']:
                                                    
                                                    addcart.append(product)
                                                    print("Product added to cart.")
                                                    
                                                    product['Quantity'] -= quantity_to_buy
                                                else:
                                                    print("Purchase Canceled.")
                                            else:
                                                print("Sorry, Not Enough Quantity Available.")
                                            break
                                    else:
                                        print("Product Not Found.")
                                
                                
                                for price in pricelst:
                                    for product in productlst:
                                        if product['price'] == price:
                                            print("Product:", product['name'])
                                            print("Category:", product['category'])
                                            print("Price:", product['price'])
                                            print("Quantity:", product['Quantity'])
                                            print("Description:", product['description'])
                                            print("==========================")
                            elif Buypro==5:

                                pricelst=[]
                                
                                for i in productlst:
                                    pricelst.append(i['price'])
                                    
                                    pricelst.sort()
                                    
                                print(pricelst)
                                
                                buy_choice = input("Do you Want Any Product (y/n): ")
                                
                                if buy_choice in ['y', 'yes']:
                                    pro_name = input("Enter Product Name To Be Bought: ")
                                    
                                    for product in productlst:
                                        if product['name'] == pro_name:
                                            quantity_to_buy = int(input("Enter Quantity to Buy: "))
                                            
                                            if quantity_to_buy <= product['Quantity']:
                                                confirm_buy = input("Are You Confirm To Buy This Product? (y/n): ")
                                                
                                                if confirm_buy in ['y', 'yes']:
                                                    
                                                    addcart.append(product)
                                                    print("Product added to cart.")
                                                    
                                                    product['Quantity'] -= quantity_to_buy
                                                else:
                                                    print("Purchase Canceled.")
                                            else:
                                                print("Sorry, Not Enough Quantity Available.")
                                            break
                                    else:
                                        print("Product Not Found.")
                                
                            elif Buypro==6:
                                
                                print(addcart)
                            elif Buypro==0:
                                print("Exit...")
                                break
                if f==0:
                    print("Invalid Login Details...")
        elif a==0:
            print("Exit")
            break
        else:
            print("Invalid Choice...")
            
        print(lst)
amazone()