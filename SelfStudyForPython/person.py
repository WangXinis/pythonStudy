#person class 


class Person:
    def __init__(self,name,job=None,pay=0):
        self.name=name
        self.job=job
        self.pay=pay
    def talk(self):
        print("Hi,I am "+self.name)
    def lastanme(self):
        return self.name.split()[-1]
    def giveRaise(self,percent):
        self.pay=int(self.pay*(1+percent))
bob=Person('Bob Smith',job="DEV",pay=10000)
sum=Person('Sum Smith')
print(bob.name,bob.pay)
print(sum.name,sum.pay)