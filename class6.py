
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
        
    def __truediv__(self,temp):
        self.hour=self.hour/temp.hour
        self.minute=self.minute/temp.minute
        self.second=self.second/temp.second
        
t1 = Time();
t2 = Time();

t1.setdata(5,4,3)
t1.disp()

t2.setdata(2,5,6)
t2.disp()

t1/t2
t1.disp()

# __add__ , __sub__ , __mul__ , __truediv__