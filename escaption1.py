try:
    a=int(input("Enter value:-"))    
    b=int(input("Enter value:-"))
    c=a/b
    print(c)
except ValueError:
    print("string naiiiiiii j chale...")
except ZeroDivisionError:
    print("0 value error")
print("keyur patel")