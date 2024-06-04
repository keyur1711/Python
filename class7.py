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
        
    def __mul__(self,t2):
    
        t4=Time();
            
        t4.hour = self.hour * t2.hour 
        t4.minute = self.minute * t2.minute 
        t4.second = self.second * t2.second 
        
        return t4
        
t1 = Time();
t2 = Time();
t3 = Time();


t1.setdata(5,4,3)
t1.disp()

t2.setdata(2,5,6)
t2.disp()

t3.setdata(7,8,9)
t3.disp()

t4=t1*t2*t3
t4.disp()
