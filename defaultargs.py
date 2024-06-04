#if your want to set degault args then must passed right to left

def emp(name="",age=0,sal=0):
    print("name",name)
    print("age",age)
    print("sal",sal)
    print("--------------------------------")
    
#default arguments    
#emp(age=89,sal = 60000,name = "aaa")
#emp("keyur",56000)
#emp("keyur",sal = 56000)
emp()