#if your want to set positional-only  args then must passed / in args

def emp(*keyur):
    print(keyur)
    print("name = " ,keyur[0])
    print("age = " ,keyur[1])
    print("sal = " ,keyur[2])
    

emp("keyur",56,56000)