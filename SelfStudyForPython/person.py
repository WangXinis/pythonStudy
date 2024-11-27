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
    def __str__(self) -> str:
        return "[Person: %s,%s,%s]"%(self.name,self.job,self.pay)
"""
bob=Person('Bob Smith',job="DEV",pay=10000)
sum=Person('Sum Smith')
print(bob.name,bob.pay)
print(sum.name,sum.pay)
"""
class Manager(Person):
    def __init__(self,name,pay=0):
        Person.__init__(self,name,'mgr',pay)
    def giveRaise(self,percent,bonus=.10):
        #self.pay=int(self.pay*(1+percent+bonus))
        Person.giveRaise(self,percent+bonus)
    def __getattr__(self,attr):
        return getattr(self,attr)

if __name__=="__main__":
    bob=Person('Bob Smith',job="DEV",pay=10000)
    sum=Person('Sum Smith')
    print(bob.name,bob.pay)
    print(sum.name,sum.pay)

    print(bob.lastanme(),sum.lastanme())
    bob.giveRaise(.10)
    print(bob.pay)
    print(sum,bob)

    #tom=Manager('Tom Doe','mgr',50000)
    tom=Manager('Tom Doe',50000)
    tom.giveRaise(.10)
    print(tom.lastanme(),tom.pay)
    print(tom)

    print("------all Tree---")
    for obj in (bob,sum,tom):
        obj.giveRaise(.10)
        print(obj)