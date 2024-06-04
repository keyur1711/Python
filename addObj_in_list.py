class Emp:
    sal=0
z=Emp();
x=Emp();
y=Emp();
lst=[]
lst.append(z)
lst.append(x)
lst.append(y)

lst.reverse()
print(lst)

print(dir(z))

print(z.__str__())
print(z)