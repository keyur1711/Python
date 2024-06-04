def maxvalue(*a):
    maxval=0
    for i in a:
        if i>maxval:
            maxval=i
    print("Maximum value is:-",maxval)
maxvalue(10,20,50)
