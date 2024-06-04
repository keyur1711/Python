a=open("abc.txt","r")

x=a.read()

a.close()

b=open("vowels.txt","w")
c=open("consonents.txt","w")

for i in x:
    if i in 'aeiouAEIOU':
        b.write(i)
    else:
        c.write(i)
b.close()
c.close()