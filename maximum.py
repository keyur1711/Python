a=int(input("enter the first value"))
b=int(input("enter the second value"))
c=int(input("enter the third value"))

if (a>b) and (a>c):
    print("First value is bigger")
elif (b>a) and (b>c):
    print("Second value is bigger")
elif (c>a) and (c>b):
    print("Third value is bigger")