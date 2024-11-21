

class FirstClass:
    def setdata(self, value):
        self.data = value
    def display(self):
        print(self.data)
x=FirstClass()
y=FirstClass()
x.setdata("king auth")
y.setdata(3.1415926)

x.display()
y.display()

x.data="wangxin"
x.display()
x.anothername="fengbi"
x.display()