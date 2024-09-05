'''
We are developing a zoo which has several kind of animals
and some of the have been housed alongside other animals.

Parent Class Animal (color, legs) attribute
SubClasses Wolf, Sheep, Snake, Parrot each takes single
attribute (color)


'''

class Animal:
    '''
    In other languages, this is called Abstract class
    WE don't instantiate from this class(no instance) but
    other classes inherit from thsi base class
    '''
    def __init__(self, color, number_of_legs):
        self.species = self.__class__.__name__
        #classes behave similar to modules
        #classes have a __name__ attribute just like modules
        #self.__class__ gives class of an object
        #the __name__ gives a string representation of class
        self.color = color
        self.number_of_legs = number_of_legs

    def __repr__(self):
        return f'{self.color} {self.species}, {self.number_of_legs} legs'
    
class Wolf(Animal):
    def __init__(self, color):
        super().__init__(color, 4)
        #invokes __init__ of Animal class, with color and default value for legs

class Sheep(Animal):
    def __init__(self, color):
        super().__init__(color, 4)

class Snake(Animal):
    def __init__(self, color):
        super().__init__(color, 0)

class Parrot(Animal):
    def __init__(self, color):
        super().__init__(color, 2)

wolf1 = Wolf('black')
sheep1 = Sheep('white')
snake1= Snake('brown')
parrot = Parrot('green')

print(wolf1.species)
print(sheep1.color)
print(snake1.number_of_legs)
print(parrot)

#another way
'''
Instead of Species inheriting from Animal class,
we have differnt legged classes that inherit from Animal
and Species inherit from these subclasses
'''
class Animal_2:
    def __init__(self, color):
        '''
        Same as above Abstract class
        Legs are now moved to subclasses
        '''
        self.species = self.__class__.__name__
        self.color = color

    def __repr__(self):
        return f'{self.color} {self.species}, {self.number_of_legs} legs'
    
class TwoLeggedAnimal(Animal_2):
    def __init__(self, color):
        super().__init__(color)
        #invokes Parent class __init__ for color
        self.number_of_legs = 2
        #fixed legs
    
class FourLeggedAnimal(Animal_2):
    def __init__(self, color):
        super().__init__(color)
        self.number_of_legs = 4

class ZeroLeggedAnimal(Animal_2):
    def __init__(self, color):
        super().__init__(color)
        self.number_of_legs = 0     

class Wolf(FourLeggedAnimal):
    '''
    Inherits from Subclass of Animal class
    '''
    def __init__(self, color):
        super().__init__(color)
        #invokes __init__ of Parent which in turn calls __init__ of Animal

class Sheep(FourLeggedAnimal):
    def __init__(self, color):
        super().__init__(color)

class Snake(ZeroLeggedAnimal):
    def __init__(self, color):
        super().__init__(color)

class Parrot(TwoLeggedAnimal):
    def __init__(self, color):
        super().__init__(color)

wolf2 = Wolf('black')
sheep1 = Sheep('white')
snake1= Snake('brown')
parrot = Parrot('green')

print(wolf2)

#yet another way
'''
'''

class Animal_3:
    '''
    Same as first one
    but number of legs is a default value instead of an attribute of __init__
    '''
    def __init__(self, color):
        self.species = self.__class__.__name__
        self.color = color
    def __repr__(self):
        return f'{self.color} {self.species}, {self.number_of_legs} legs'

class Wolf(Animal_3):
    number_of_legs = 4
    def __init__(self, color):
        super().__init__(color)

class Sheep(Animal_3):
    number_of_legs = 4
    def __init__(self, color):
        super().__init__(color)

class Snake(Animal_3):
    number_of_legs = 0
    def __init__(self, color):
        super().__init__(color)

class Parrot(Animal_3):
    number_of_legs = 2
    def __init__(self, color):
        super().__init__(color)

wolf1 = Wolf('black')
sheep3 = Sheep('white')
snake1= Snake('brown')
parrot = Parrot('green')

print(sheep3)

#another way
'''
This time, we have default sound for each class
'''

class Animal():
    def __init__(self, color, number_of_legs):
        self.species = self.__class__.__name__
        self.color = color
        self.number_of_legs = number_of_legs

    def __repr__(self):
        return f'{self.sound}--{self.color} {self.species}, {self.number_of_legs} legs'


class Wolf(Animal):
    sound = 'awooo'

    def __init__(self, color):
        super().__init__(color, 4)


class Sheep(Animal):
    sound = 'baa'

    def __init__(self, color):
        super().__init__(color, 4)


class Snake(Animal):
    sound = 'hiss'

    def __init__(self, color):
        super().__init__(color, 0)


class Parrot(Animal):
   sound = 'Polly wants a cracker!'

   def __init__(self, color):
       super().__init__(color, 2)

wolf1 = Wolf('black')
sheep3 = Sheep('white')
snake4= Snake('brown')
parrot = Parrot('green')

print(snake4)

'''
So as you can observe, OOPS can be implemented many ways
It's all about how flexible you want this to be
'''