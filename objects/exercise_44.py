'''
Animal and Subclasses were defined in previos exercise
Now, we will work on Cages to keep Animals

A Cage class is an empty list with a max limit of Animals
that can be stored.
Each cage has a number, a method to add_animals
'''

class Simple_Cage:
    '''
    Solution sounds similar to Bowl class and Scoop class
    in earlier exercises
    '''
    def __init__(self, id_number):
        self.id_number = id_number
        self.animals = []

    def add_animals(self, *animals):
        for one_animal in animals:
            self.animals.append(one_animal)
    
    def __repr__(self):
        output = f'Cage {self.id_number}\n'
        output += '\n'.join('\t'+ str(animal)
                            for animal in self.animals)
        return output
#test
simple_cage1 = Simple_Cage('C001')

#a better way
'''
Hardcode maximum number of animals in a cage
Same as Bowl and Scoop
'''
class Fixed_Cage:
    max_animals = 3

    def __init__(self, id_number):
        self.id_number = id_number
        self.animals = []

    def add_animals(self, *animals):
        for one_animal in animals:
            if len(self.animals) < self.max_animals:
                self.animals.append(one_animal)

    def __repr__(self):
        output = f'Cage {self.id_number}\n'
        output += '\n'.join('\t' + str(animal)
                            for animal in self.animals)
        return output
    
class BigCage(Fixed_Cage):
    max_animals = 5

fixed_cage1 = Fixed_Cage('FC001')
BigCage1 = BigCage('BC001')

#a much better way with space requirments set
'''
for this part we have defined Animal class from previous exercise
We can import it as well
For subclasses, we have a space_required, that adds to the size of list
of occupants

'''
class Animal:
    def __init__(self, color, number_of_legs):
        self.species = self.__class__.__name__
        self.color = color
        self.number_of_legs = number_of_legs
    def __repr__(self):
        return f'{self.color} {self.species}, {self.number_of_legs} legs'
    
class Wolf(Animal):
    space_required = 10
    #wolf needs 10 unit area
    #the rest is same
    def __init__(self, color):
        super().__init__(color, 4)

class Sheep(Animal):
    space_required = 5
    def __init__(self, color):
        super().__init__(color, 4)

class Snake(Animal):
    space_required = 2
    def __init__(self, color):
        super().__init__(color, 0)

class Parrot(Animal):
    space_required = 1
    def __init__(self, color):
        super().__init__(color, 2)

#test
wolf1 = Wolf('black')
sheep1 = Sheep('white')
snake1= Snake('brown')
parrot1 = Parrot('green')

fixed_cage1.add_animals(wolf1,sheep1)
BigCage1.add_animals(snake1,parrot1)

# print(fixed_cage1)
# print(BigCage1)

class NotEnoughSpaceError(Exception):
    pass

class DangerousAssignmentError(Exception):
    pass

#defining a dict that sets relation b/w various animals
#An animal is compatible with participants of list of value
animal_safety = {Wolf: [Wolf, Snake, Parrot],
                 Sheep: [Sheep, Snake, Parrot],
                 Snake: [Wolf, Sheep],
                 Parrot: [Wolf, Sheep]}

class Safe_Cage:
    total_space = 20

    def __init__(self, id_number):
        self.id_number = id_number
        self.animals = []
        

    '''
    def add_animals(self, *animals):
        for one_animal in animals:
            if self.space_used() + one_animal.space_required > self.total_space:
                raise NotEnoughSpaceError(
                    f'Not enough room for your {one_animal}'
                )
            self.animals.append(one_animal)
    '''
    def add_animals(self, *animals):
        for one_animal in animals:
            for one_current_resident in self.animals:
                if type(one_animal) not in animal_safety[type(one_current_resident)]:
                    raise DangerousAssignmentError(
                        f'You cannot put a {type(one_animal)} with a {type(one_current_resident)}'
                    )
                self.animals.append(one_animal)


    def space_used(self):
        return sum(one_animal.space_required
                   for one_animal in self.animals)       
     
    def __repr__(self):
        output = f'Cage {self.id_number}\n'
        output += '\n'.join('\t' + str(animal)
                            for animal in self.animals)
        return output
    
class Safe_BigCage(Safe_Cage):
    total_space = 30

wolf2 = Wolf('black')
sheep2 = Sheep('white')
snake2= Snake('brown')
parrot2 = Parrot('green')

safe_cage1 = Safe_Cage('SFC001')
safe_big_cage1 = Safe_BigCage('SFBC001')

safe_cage1.add_animals(sheep2)
# safe_cage1.add_animals(wolf2)
print(safe_cage1)