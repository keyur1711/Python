#if your want to set positional-only  args then must passed / in args

def emp(**keyur):
    print(keyur["name"])
    

emp(name = "keyur",age = 56,sal =56000)