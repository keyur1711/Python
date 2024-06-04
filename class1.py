class Emp():
   
    def setdata(self,name,age,sal):
        self.name = name
        self.age = age
        self.sal = sal
    def disp(self):
        print(self.name)
        print(self.age)
        print(self.sal)
        print("-----------------------------------")
x = Emp()
y = Emp()

x.setdata("aaa",56,56000)
x.disp()

y.setdata("bbb",25,75000)
y.disp()
