'''
z=[1,2,3,4,5,6,7,8,9,0]
print(z)'''

'''
z=[1,2,3,4,5,6,7,8,9,0]
z[2]=100;
print(z)'''

'''
z=[1,2,3,4,5,6,7,8,9,0]
print(z[-5])'''

'''
z=[1,2,'keyur',4,5,'patel',7,8,9,99.78]
print(type(z[9]))'''
lst = [1,2,3,4,5,6,7,8,9]
#print(dir(lst))

#help(lst.append)

lst.append(100)
print(lst)
lst.insert(5,200)
print(lst)

print(lst.index(8))
print(lst.count(5))
#lst.sort(reverse=True)
lst.reverse()
print(lst)

#lst.pop(0)
#print(lst)

lst.remove(100)
print(lst)