class Time():
    def __init__(self,hour,minute,second):
        self.hour = hour
        self.minute = minute
        self.second = second
    def __str__(self):
        print(self.hour)
        print(self.minute)
        print(self.second)
        
        return ""

z=Time(4,5,6)

print(z)