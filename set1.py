s={1,2,3,1,1,1,1,1,1,4,5,6,7,8,9}
s1={1,2,1,2}

#print(s)
#print(type(s))
#print(dir(s))

s.add(100)
print(s)

s.remove(100)
print(s)

#s.pop()
#print(s)
print(s.union(s1))
#print(s.intersection(s1))
#s.intersection_update(s1)
#print(s.difference(s1))
#s.difference_update(s1)
print(s1.issubset(s))
print(s.issuperset(s1))
