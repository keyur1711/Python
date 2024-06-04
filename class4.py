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
        
    def add(self,temp,temp2):
        t3.hour=self.hour+temp.hour+temp2.hour
        t3.minute=self.minute+temp.minute + temp2.minute
        t3.second=self.second+temp.second + temp2.second
        
            
t1 = Time();
t2 = Time();
t3 = Time();
t1.setdata(5,4,3)
t1.disp()

t2.setdata(2,5,6)
t2.disp()

t3.setdata(4,7,3)
t3.disp()

t3.add(t1,t2)
t3.disp()

