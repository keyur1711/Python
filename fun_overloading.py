class demo:
    def demo(s):
        print("First")
        
    def demo(s,a):
        print("second")
class demo2(demo):
    def demo(s,a,c):
        print("Third")
k=demo2();
k.demo("","")