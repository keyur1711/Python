from threading import Thread

import time
def demo(a,b,c):
    print("hello")
    print(a,b,c)
    time.sleep(3)
def test():
	print("test")
	
    
t1 = Thread(target = demo,args=(1,2,3));
t2 = Thread(target = test);


t1.start()
t2.start()
help(Thread)


