import copy 
class MobilePhone:
    def __init__(self,cpu,screen):
        self.cpu=cpu
        self.screen=screen
class CPU:
    def calculate(self):
        print("cup计算","算一个12345")
        print("CPU对象",self)
class Screen:
    def show(self):
        print("显示一个好看的画面，太美")
        print("屏幕对象",self)
c=CPU()
s=Screen()
m=MobilePhone(c,s)
m.cpu.calculate()
n=m
print(m,n)
m2=copy.copy(m)
print(m,m2)
m.cpu.calculate()
m2.cpu.calculate()
m3=copy.deepcopy(m)
m3.cpu.calculate()
m.screen.show()