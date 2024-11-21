from SecondClass import SecondClass
print("------------------第三个类文件------------------------")

class ThirdClass(SecondClass):
    def __init__(self,value):
        self.data=value
    def __add__(self,other):
        return ThirdClass(self.data+other)
    def __str__(self):
        return ('[ThirdClass]%s'%self.data)
    def mul(self,other):
        self.data*=other



print(ThirdClass.__mro__)
a=ThirdClass('abc')
print("xxxxx")
a.display()
print(a)

b=a+'xyz'
b.display()

a.mul(3)
a.display()