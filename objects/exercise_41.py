'''
Inheritance forms an IS-A relationship. It removes repeatition.
example: Car IS A vehicle, House IS A building

Use it when we want to classes that are similar to one another.

so, a PARENT class is one which contains a GENERAL behavior,
while a CHILD class is one which contains a SPECIFIC behavior alongwitA
the GENERAL behavior.

Instance can be of either of them.
Example: An Employee is a PERSON. So person will be parent class, employee
will be child class. But, Employee needs an ID number, which Person doesn't
have, so that will be the sole addition alongwith specific methods.

And, as always, remember ICPO (instance, class, parent, object)

class Person:
    def __init__(self,name):
        self.name = name
    def greet(self):
        print(f'Hello, {self.name}')

class Employee(Person):
    def __init__(self,name, employee_ID):
        self.name = name
        self.ID = employee_ID

#creating an instance of Employee
emp1 = Employee('emp1',243)
#calling method on instance of Employee
#method is defined in Parent class
emp1.greet()

If you observe, we had to set self.name in __init__ of Employee. If we don't do
so, the attribute will never be set for Employee even though it is Child of Person
class and we did define it there.

Well, that's Python using ICPO. It looks for __init__ in the instance, then class.
The __init__ of class is executed, and it doesn't look for __init__ of Parent class.

But, this violates the DRY rule(don't repeat yourself). So, a solution is to use SUPER

class Employee(Person):
    def __init__(self,name,employee_ID):
        super().__init__(name)
        self.ID = employee_ID

SUPER allows us to invoke a method on a parent object without explicitly naming that parent.
'''

'''
#sample
For this, we will create a XL version of our Bowl
The Parent Class is the same
WE add a new Child class, and modify its attribute
'''
class Scoop:
    def __init__(self, flavor):
        self.flavor = flavor
    
class Bowl:
    max_scoops = 3

    def __init__(self):
        self.scoops = []
    
    def add_scoops(self, *new_scoops):
        for one_scoop in new_scoops:
            if len(self.scoops) < self.max_scoops:
                self.scoops.append(one_scoop)
    
    def __repr__(self):
        return '\n'.join(s.flavor
                         for s in self.scoops)


class BigBowl(Bowl):
    '''
    Child Class that can take 5 scoops
    '''
    max_scoops = 5

#sample
Xl_bowl = BigBowl()
[Xl_bowl.add_scoops(Scoop(item))
    for item in ('vanila','chocolate','pineapple','cookie','strawberry','banana')]
#creating multiple instances using comprehension

print(Xl_bowl)


'''
#sample
Envelope class with two attributes, weight and was_sent(default False)
and three methods (send, add_postage, postage_needed)
'''
class NotEnoughPostageError(Exception):
    pass

class Envelope:
    postage_multiplier = 10
    #postage is a multiplier of weight and this value

    def __init__(self, weight):
        #defines a new envelope that has weight, and a default attribute
        self.weight = weight
        self.postage = 0
        self.was_sent = False
    
    def add_postage(self, amount):
        #add the amount required to send the package
        self.postage += amount

    def send(self):
        #send if enough postage is added
        if self.postage >= self.weight * self.postage_multiplier:
            self.was_sent = True
        else:
            raise NotEnoughPostageError('Not enough Postage')

#child class for large envelopes
class BigEnvelope(Envelope):
    postage_multiplier = 15

env1 = Envelope(10)
env1.add_postage(101)
env1.send()
print(env1.was_sent)

'''
#sample
A Phone class, that has a dial method to simulate a phone number
A SmartPhone child class, that uses Phone.dial method but implements
own run_app method
A iPhone Child class to implement run_app method, and its own dial method
that invokes parent's dial method.
'''
class Phone:
    def __init__(self):
        pass

    def dial(self, number):
        return f'Dialing {number}'
    
class SmartPhone(Phone):
    def run_app(self, app_name):
        return f'RUNNING an app: {app_name}'

class iPhone(SmartPhone):
    def run_app(self, app_name):
        return super().run_app(app_name).lower()

phone = Phone()
print(phone.dial(344567))
s_phone = SmartPhone()
print(s_phone.run_app('dialer'))
i_phone = iPhone()
print(i_phone.run_app('dialer'))

'''
#sample
A Bread class that has default values for nutrition
A WholeWheatBread child class that has different values for it
A RyeBread Child class,
All these classes have same method get_nutrition
'''


class Bread:
    def __init__(self):
        #nutrition per slice
        self.calories = 66
        self.carbs = 12
        self.sodium = 170
        self.sugar = 1
        self.fat = 0.8

    def get_nutrition(self, number_of_slices):
        return {key: value*number_of_slices
                for key, value in vars(self).items()}
        #vars(object) creates a dict of the object
    
class WholeWheatBread(Bread):
    #we use () to indicate class or classes from which our new class inherits
    def __init__(self):
        self.calories = 67
        self.carbs = 12
        self.sodium = 138
        self.sugar = 1.4
        self.fat = 1

class RyeBread(Bread):
    def __init__(self):
        self.calories = 67
        self.carbs = 12
        self.sodium = 172
        self.sugar = 1
        self.fat = 0.8

print(Bread().get_nutrition(2))
print(WholeWheatBread().get_nutrition(2))
print(RyeBread().get_nutrition(2))