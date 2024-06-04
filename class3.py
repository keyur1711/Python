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
        
    def add(self,temp):
        t3=Time();
        t3.setdata(0,0,0)
        
        t3.hour=self.hour+temp.hour
        t3.minute=self.minute+temp.minute
        t3.second=self.second+temp.second
        
        return t3
    
t1 = Time();
t2 = Time();

t1.setdata(5,4,3)
t1.disp()

t2.setdata(2,5,6)
t2.disp()

t3 = t1.add(t2)
t3.disp()

