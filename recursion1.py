i=1

def demo():
    global i
    print("recursion",i)
    i=i+1
    demo()
    
    
demo()
