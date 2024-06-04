g=0
def sss():
    global g
    while g<=10:
        yield g
        g=g+1
		#return i
	
	

z = sss()
print(next(z))
print(next(z))
