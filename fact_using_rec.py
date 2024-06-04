def fact(a):
    if a == 1:
        return a
    else:
        return a*fact(a-1)
        
z = fact(5)
print(z)
