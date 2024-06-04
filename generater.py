'''
def gen():
    for i in range(1000000000000000000000000000000000000000000000000000000000000):
        yield(i)


z = gen()
print(z)
print(next(z))
print(next(z))
print(next(z))
'''
def m1(h,x):
    print("Before function")
    h()
    print("After function")

def m2():
    print("This Is m2 Function")
def m3():
    x()
    print("This Is m2 Function")
    
m1(m2,m3)