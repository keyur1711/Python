lst=[]
lst2=[]
queslist=[]
counter=0

while True:
    print("1. Admin ")
    print("2. Student ")
    print("3. Exit ")
    
    a=int(input("Enter Your Choice:-"))
    
    if a==1:
        print("1. Register")
        print("2. Login")
        
        admin=int(input("Chose Register Or Login"))
        
        if admin==1:
            dic={}
            email=input("Enter Email:-")
            password=input("Enter Password:-")
            
            dic["email"]=email
            dic["password"]=password
            lst.append(dic)
        elif admin==2:
            Lemail=input("Enter Your Registerd Email:-")
            Lpassword=input("Enter Your Registerd Password:-")
            f=0
            Qlst=[]
            for i in lst:
                if i['email']==Lemail:
                    f=1
                    print("Login Successfully...")
                    while True:
                        print("1.Add Question:-")
                        print("2.Update Question:-")
                        print("3.Remove Question:-")
                        print("4.Display Question:-")
                        print("5. Exit")
                        
                        Que=int(input("Enter Your Choice:-"))

                        if Que==1:
                            Question=input("Enter The Questions:-")
                            option1=input("Enter First Option:-")
                            option2=input("Enter Second Option:-")
                            option3=input("Enter Third Option:-")
                            option4=input("Enter Fourth Option:-")
                            
                            
                            rightOp=input("Right Ans is..")
                            questdic={} 
                            if rightOp ==option1 or rightOp==option2 or rightOp ==option3 or rightOp==option4:
                                questdic['Que']=Question
                                questdic['ans']=rightOp
                                questdic["op"] = [option1,option2,option3,option4]
                                questdic["id"] = counter
                                counter +=1
                                
                                queslist.append(questdic)  
                        elif Que==2:
                            que=int(input("Enter Your Question id To Update The Question:-"))
                            
                            for i in queslist:
                                if i['id']==que:
                                    upque=input("Enter New Question:-")
                                    option1=input("Enter First Option:-")
                                    option2=input("Enter Second Option:-")
                                    option3=input("Enter Third Option:-")
                                    option4=input("Enter Fourth Option:-")
                                    
                                    rightOp=input("Right Ans is..")
                                    
                                    if rightOp ==option1 or rightOp==option2 or rightOp ==option3 or rightOp==option4:
                                        questdic['Que']=upque
                                        questdic['ans']=rightOp
                                        questdic['op']=[option1,option2,option3,option4]
                        elif Que==3:
                            delid=int(input("Enter The Question Id To Be Deleted:-"))
                            
                            for i in queslist:
                                if i['id']==delid:
                                    queslist.pop(delid)
                                                                 
                        elif Que==4:
                            print(queslist)
                        elif Que==5:
                            print("Exit...")
                            break
                        else:
                            print("Invalid Choice...")
                            break
            if f==0:
                print("Invalid Email")
    elif a==2:
        print("1. Register")
        print("2. Login")
        
        student=int(input("Chose Register Or Login"))
        
        if student==1:
            dic={}
            email=input("Enter Email:-")
            password=input("Enter Password:-")
            
            dic["email"]=email
            dic["password"]=password
            lst2.append(dic)
            
        elif student==2:
            Lemail=input("Enter Your Registerd Email:-")
            Lpassword=input("Enter Your Registerd Password:-")
            f=0
            for i in lst2:
                if i['email']==Lemail:
                    f=1
                    print("Login Successfully...")
                    total=0
                    for i in queslist:
                        print(i['Que'])
                        print(i['op'][0])
                        print(i['op'][1])
                        print(i['op'][2])
                        print(i['op'][3])
                        rightop=input("Enter Right Option:-")
                        
                        if rightop == i['ans']:
                            total=total+1
                    print(total,"/",len(queslist))
            if f==0:
                print("Invalid Email")
    elif a==3:
        print("Exit...")
        break
    else:
        print("Invalid Choice")
    
    print(lst)
    print(lst2)