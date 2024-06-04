def emp(name,age,sal):
    print("name",name)
    print("age",age)
    print("sal",sal)
    print("--------------------------------")
    
#keyword arguments    
emp(age=89,sal = 60000,name = "aaa")
emp("aaa",sal = 65000,age = 89)
#emp("aaa",65000,age = 89)
#emp("aaa",age = 89,56000)
emp("aaa",age = 89,sal =56000)