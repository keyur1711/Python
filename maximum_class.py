class Emp:
    sal=0
    name=""
    age=0
z=Emp();
z.sal=120000
z.name='yash'
z.age=20
print(z.sal)

a=Emp()
a.sal=15000
a.name='keyur'
a.age=21
print(a.sal)

if z.sal>a.sal:
    print("Z sal is Max",z.sal)
    print(z.sal)
    print(z.name)
    print(z.age)
else:
    print("A sal is Max",a.sal)
    print(a.sal)
    print(a.name)
    print(a.age)