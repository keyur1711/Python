t = (1,1,1,1,"hello",2,3,4,5,6,7,8,9)


print(t)
print(type(t))

print(dir(t))

help(t.count)
print(t.count(1))
print(t.index(3))

t[3]=56
print(t)