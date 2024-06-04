class Time():
   
    def setdata(self,hour,minute,second):
        self.hour = hour
        self.minute = minute
        self.second = second
    def disp(self):
        print("Hour=",self.hour)
        print("Minute=",self.minute)
        print("Second=",self.second)
        print("-----------------------------------")
x = Time()
y = Time()

x.setdata(5,25,35)
x.disp()

y.setdata(4,24,34)
y.disp()
