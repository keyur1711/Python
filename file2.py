a=open("two.txt","r")
b=open("three.txt","r")

z=a.read()
x=b.read()

c=open("four.txt","a")
y=c.write(z+" "+x+" "+" "+"jay shree ram")

a.close()
b.close()
c.close()