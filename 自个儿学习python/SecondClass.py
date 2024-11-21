# 学习python
"""在这里需要两种导入方式"""
import FirstClass
#from FirstClass import FirstClass


class SecondClass(FirstClass.FirstClass):
    def display(self):
        print("Current Value：%s"%self.data)

z=SecondClass()
z.setdata(20)
z.display()
