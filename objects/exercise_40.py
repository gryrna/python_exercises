'''
@dataclass
This decorator reduces redundancy and let's us focus more
on code
It implements __init__, __repr__
'''

from typing import List
from dataclasses import dataclass, field

@dataclass
class Scoop:
    flavor: str
    #to indicate that 'flavor' attribute only takes string

@dataclass
class Bowl:
    max_scoops = 3
    #this can be defined on the __init__ or class decorator
    #but, doing so will create different bowl. We got to have a standard bowl


    scoops : List[Scoop] = field(default_factory=list)
    #the List type, when used alone, is a simple list of any type
    #when used with [] it indicates that all elements of List will be objects of class Scoop
    #the default_factory parameter tells dataclass to create a new instance and not the existing one

    def add_scoops(self, *new_scoops):
        for one_scoop in new_scoops:
            if len(self.scoops) < Bowl.max_scoops:
                self.scoops.append(one_scoop)
    
    def _repr__(self):
        return '\n'.join(s.flavor for s in self.scoops)

'''
Class variables in Python can be modified 2 ways
using class.attribute_name or instance.attribute_name
Former updates it for all new instances, later changes only
for the instance it is called on

Methods are almost always defined on the class not the instances
'''

'''
#sample
A Person class with a Class Attribute 'population'
It increase every time we create a new instance of Person class
'''
class Person:
    population = 0

    def __init__(self, name):
        self.name = name
        Person.population += 1

    def __del__(self):
        Person.population -= 1

#sample
p1 = Person('A')
p2=Person('B')

print(p2.population)
#population is not on instance but on class

p2.__del__()
#removing the person
print(Person.population)

'''
#sample
A class Transaction where each instance represents either a deposit or a withdrawal
Deposit is +
Withdrawal is -
'''

class Transaction:
    balance = 0

    def __init__(self, amount):
        self.amount = amount
        Transaction.balance += amount

Transaction(+50)
Transaction(-10)
print(Transaction.balance)

'''
How Python searches for attributes?
INSTANCE
CLASS
PARENTS
OBJECT

So, for a.b
Python first searches 'a' for 'b'
If not found, then it searches for class of 'a' for 'b' i.e. type(a).b
If not found, then it searches for parent class of class of 'a' for 'b'
Lastly, it searches in ulitmate parent of all in Python, object

Object exists so that other classes can inherit from it.
'''