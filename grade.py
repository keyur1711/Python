a=int(input("Enter the first value"))
b=int(input("Enter the Second value"))
c=int(input("Enter the Third value"))
d=int(input("Enter the Fourth value"))
e=int(input("Enter the Fifth value"))

total = a+b+c+d+e
print("The sum is=",total)

avg= (total/500)*100
print("The avarage is",avg)

if (avg>=90):
    print("Grade A:")
elif (avg>=80):
    print("Grade B:")
elif (avg>=60):
    print("Grade C:")
elif (avg>=50):
    print("Grade D:")
else:
    print("Fail")