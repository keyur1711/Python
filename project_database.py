import mysql.connector as mc

M = mc.connect(host="localhost",user="root",password="1711",database="teach")

teach=[]
stud=[]
counter=0

class Teacher():
    global M
    def reg(self):
        
        tdic={}
        self.email = input("Enter your Email:-")
        self.password = input("Enter your Password:-")
            
        

        teach.append(tdic)
        Q="insert into emp values('"+self.email+"','"+self.password+"');"
        print(Q)
        x = M.cursor()
        x.execute(Q)
        M.commit()
        
    def log(self):
        Q = "select * from emp"
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
                    Que=input("Enter The Question:-")
                    op1=input("Enter The First Option:-")
                    op2=input("Enter The Second Option:-")
                    op3=input("Enter The Third Option:-")
                    op4=input("Enter The Fourth Option:-")
                    
                    Rop=input("Enter Right Option:-")
                    
                    
                    
                    if Rop==op1 or Rop==op2 or Rop==op3 or Rop==op4:
                        
                        Q="insert into tQue2(Questions ,Option1  ,Option2,Option3,Option4  ,RightAns  ) values('"+Que+"','"+op1+"','"+op2+"','"+op3+"','"+op4+"','"+Rop+"');"
                        print(Q)
                        x = M.cursor()
                        x.execute(Q)
                        M.commit()
                    else:
                        print("Please Enter Valid Right Ans..")
                elif a==2:
                    que=input("Enter Your Question To Update:-")
                    
                    Q="select * from tQue2 where Questions='"+que+"'"
                    x=M.cursor()
                    x.execute(Q)
                    
                    
                    data = x.fetchall()
                    print(data)
                    
                    if data[0][1]==que:
                        upque=input("Enter New Question:-")
                        op1=input("Enter First Option:-")
                        op2=input("Enter Second Option:-")
                        op3=input("Enter Third Option:-")
                        op4=input("Enter Fourth Option:-")
                        
                        rightOp=input("Right Ans is..")
                        
                        if rightOp ==op1 or rightOp==op2 or rightOp==op3 or rightOp==op4:
                            d={'Que':upque,'ans':rightOp,'op':[op1,op2,op3,op4]}
                            
                            Q="update tQue2 set Questions='"+upque+"',Option1='"+op1+"',Option2='"+op2+"',Option3='"+op3+"',Option4='"+op4+"',RightAns='"+rightOp+"' where Questions='"+que+"'"
                            x=M.cursor()
                            x.execute(Q)
                            M.commit()
                elif a==3:
                    
                    delque=input("Enter The Question To Be Deleted:-")
                    
                    Q="select * from tQue2 where Questions='"+delque+"'"
                    x=M.cursor()
                    x.execute(Q)
                    
                    
                    data = x.fetchall()
                    print(data)
                    
                    if data[0][1]==delque:
                        Q="delete from tQue2 where Questions='"+delque+"'"
                        x = M.cursor()             
                        x.execute(Q)
                        M.commit()
                                                             
                elif a==4:
                    Q="select * from tQue2"
                    x = M.cursor()
                    x.execute(Q)
                    
                    data=x.fetchall()
                    print(data)
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
        
        
        self.email = input("Enter your Email:-")
        self.password = input("Enter your Password:-")
            
        

        
        Q="insert into student values('"+self.email+"','"+self.password+"');"
        print(Q)
        x = M.cursor()
        x.execute(Q)
        M.commit()
    
    def log(self):
        Q = "select * from student"
        x = M.cursor()
        x.execute(Q)
        
        data = x.fetchall()
        print(data)
        
        self.email = input("Enter your Registerd Email:-")
        self.password = input("Enter your Registerd Password:-")
        
        for i in data:
            if i[0]==self.email:
                print("Login Successfully...")
                
                total=0
                Qque="select * from tQue2"
                y = M.cursor()
                y.execute(Qque)
                
                data = y.fetchall()
                print(data)
                
                for i in data:
                    print(i[1])
                    print(i[2])
                    print(i[3])
                    print(i[4])
                    print(i[5])
                    rightop=input("Enter Right Option:-")
                    
                    if rightop == i[6]:
                        total=total+1
                print(total,"/",len(data))   
                break
        else:
            print("Invalid Email And Password...")
             
while True:
    print("1. Admin ")
    print("2. Student ")
    print("3. Exit ")
    
    a=int(input("Enter Your Choice:-"))
    
    if a==1:
        
        t = Teacher()
        while True:
            print("1. Register")
            print("2. Login")
            print("3. Exit")
            Tr=int(input("Enter your Choice:-"))
            
            if Tr==1:
                t.reg()
            elif Tr==2:
                
                t.log()
                t.menu()
            elif Tr==3:
                print("Exit")
                break
        
    elif a==2:
        
        s = Student()
        while True:
            print("1. Register")
            print("2. Login")
            print("3. Exit")
            Sr=int(input("Enter your Choice:-"))
            
            if Sr==1:
            
                s.reg()
            elif Sr==2:
                s.log()
            elif Sr==3:
                print("Exit")
                break
            
    elif a==3:
        print("Exit")
        break


