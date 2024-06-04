import mysql.connector as mc


M = mc.connect(host="localhost",user="root",password="1711",database="keyur")

users_no=input("Enter The No:-")
users_name=input("Enter The Name:-")
users_email=input("Enter The Email:-")

Q="insert into python values('"+users_no+"','"+users_name+"','"+users_email+"');"
print(Q)
x = M.cursor()
x.execute(Q)
M.commit()