#if your want to set positional-only  args then must passed / in args

def emp(*,name,age,sal,/):
    print("name",name)
    print("age",age)
    print("sal",sal)
    print("--------------------------------")
emp("keyur",56,56000)
emp(name ="keyur",age = 56,sal = 56000)