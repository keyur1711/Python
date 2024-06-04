from threading import Thread
import time
import threading
def demo():
    #time.sleep(3)
    print("hello",threading.current_thread())
    time.sleep(3)
    print("Bye...")
def test():
    #time.sleep(3)
    print("test",threading.current_thread())
def test2():
    #time.sleep(3)
    print("world",threading.current_thread())


t1 = Thread(target = demo);
t2 = Thread(target = test);
t3 = Thread(target = test2);


t1.start()
t2.start()
t3.start()



print("bye from main",threading.current_thread())