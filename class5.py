class Time():

    def setdata(self,hour,minute,second):
        self.hour = hour
        self.minute = minute
        self.second = second
    def disp(self):
        print("Hour=",self.hour)
        print("Minute=",self.minute)
        print("Second=",self.second)
        print("=============")
        
def add(t1,temp):
        
    t1.hour=t1.hour+temp.hour
    t1.minute=t1.minute+temp.minute 
    t1.second=t1.second+temp.second 
        
            
t1 = Time();
t2 = Time();

t1.setdata(5,4,3)
t1.disp()

t2.setdata(2,5,6)
t2.disp()

add(t1,t2)
t1.disp()