a=open("fifth.txt","r")

x=a.read()

a.close()

b=open("sixth.txt","w")
c=open("seventh.txt","w")

for i in x:
    if int(i)%2==0:
        c.write(i)
    else:
        b.write(i)
        
b.close()
c.close()