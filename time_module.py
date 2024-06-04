class Time:
    def __init__(self,hour,minute):
        self.hour= hour
        self.minute= minute
    def __str__(self):
        print("Hour is =",self.hour)
        print("Minute is =",self.minute)
        