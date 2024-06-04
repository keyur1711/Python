teach=[]
stud=[]
counter=0
Qdic={}
Qlst=[]
class Teacher():
    def reg(self):
        
        tdic={}
        self.email = input("Enter your Email:-")
        self.password = input("Enter your Password:-")
            
        tdic['email']=self.email
        tdic['password']=self.password

        teach.append(tdic)
    
    def log(self):
        self.email = input("Enter your Registerd Email:-")
        self.password = input("Enter your Registerd Password:-")
        
        for i in teach:
            if i['email']==self.email:
                print("Login Successfully...")
                break
        else:
            print("Invalid Email And Password...")
    def menu(self):
        def Questionlab(a):
                if a==1:
                    Que=input("Enter The Question:-")
                    op1=input("Enter The First Option:-")
                    op2=input("Enter The Second Option:-")
                    op3=input("Enter The Third Option:-")
                    op4=input("Enter The Fourth Option:-")
                    
                    Rop=input("Enter Right Option:-")
                    Qdic={}
                    
                    
                    if Rop==op1 or Rop==op2 or Rop==op3 or Rop==op4:
                        Qdic['Question']=Que
                        Qdic['option']=[op1,op2,op3,op4]
                        Qdic['ans']=Rop
                        global counter
                        Qdic['id']= counter
                        
                        counter+=1
                        
                        Qlst.append(Qdic)
                elif a==2:
                    que=int(input("Enter Your Question id To Update The Question:-"))
                            
                    for i in Qlst:
                        if i['id']==que:
                            upque=input("Enter New Question:-")
                            op1=input("Enter First Option:-")
                            op2=input("Enter Second Option:-")
                            op3=input("Enter Third Option:-")
                            op4=input("Enter Fourth Option:-")
                            
                            rightOp=input("Right Ans is..")
                            
                            if rightOp ==op1 or rightOp==op2 or rightOp==op3 or rightOp==op4:
                                d={'Que':upque,'ans':rightOp,'op':[op1,op2,op3,op4]}
                                Qlst[i['id']]=d
                elif a==3:
                    delid=int(input("Enter The Question Id To Be Deleted:-"))
                    
                    for i in Qlst:
                        if i['id']==delid:
                            Qlst.pop(delid)
                                                             
                elif a==4:
                    print(Qlst)
                elif a==0:
                    return 0;
                else:
                    print("Invalid Choice...")
            
        while True:
            print("1.Add Question:-")
            print("2.Update Question:-")
            print("3.Remove Question:-")
            print("4.Display Question:-")
            print("0. Exit")
            
            a= int(input("Enter Your Choice:-"))
            z=Questionlab(a)
            if z==0:
                break
            
            
            
                        
class Student():
    def reg(self):
        
        tdic={}
        self.email = input("Enter your Email:-")
        self.password = input("Enter your Password:-")
            
        tdic['email']=self.email
        tdic['password']=self.password

        stud.append(tdic)
    
    def log(self):
        self.email = input("Enter your Registerd Email:-")
        self.password = input("Enter your Registerd Password:-")
        
        for i in stud:
            if i['email']==self.email:
                print("Login Successfully...")
                total=0
                
                for i in Qlst:
                    print(i['Question'])
                    print(i['option'][0])
                    print(i['option'][1])
                    print(i['option'][2])
                    print(i['option'][3])
                    rightop=input("Enter Right Option:-")
                    
                    if rightop == i['ans']:
                        total=total+1
                print(total,"/",len(Qlst))
                
                
        else:
            print("Invalid Email And Password...")
             
while True:
    print("1. Admin ")
    print("2. Student ")
    print("3. Exit ")
    
    a=int(input("Enter Your Choice:-"))
    
    if a==1:
        
        t = Teacher()
        t.reg()
        t.log()
        t.menu()
        print(teach)
    elif a==2:
        s = Student()
        
        s.reg()
        s.log()
        print(stud)
    elif a==3:
        break
