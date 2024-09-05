'''
Beyond previos exercise,
'''

class Zoo:
    def __init__(self):
        self.cages = []
    
    def add_cages(self, *cages):
        for one_cage in cages:
            self.cages.append(one_cage)

    def __repr__(self):
        return '\n'.join(str(one_cage)
                         for one_cage in self.cages)

    def animals_by_color(self, color):
        return [one_animal
                for one_cage in self.cages
                for one_animal in one_cage.animals
                if one_animal.color == color]
    
    def animals_by_legs(self, number_of_legs):
        return [one_animal
                for one_cage in self.cages
                for one_animal in one_cage.animals
                if one_animal.number_of_legs == number_of_legs]
    
    def number_of_legs(self):
        return sum(one_animal.number_of_legs
                   for one_cage in self.cages
                   for one_animal in one_cage.animals)
    

#beyond 1

class Animal:
    def __init__(self, color, number_of_legs):
        self.species = self.__class__.__name__
        self.color = color
        self.number_of_legs = number_of_legs

    def __repr__(self):
        return f'{self.color} {self.species}, {self.number_of_legs} legs'

class Wolf(Animal):
    def __init__(self, color):
        super().__init__(color, 4)

class Sheep(Animal):
    def __init__(self, color):
        super().__init__(color, 4)

class Snake(Animal):
    def __init__(self, color):
        super().__init__(color, 0)

class Parrot(Animal):
    def __init__(self, color):
        super().__init__(color, 2)

class Cage:
    def __init__(self, id_number):
        self.id_number = id_number
        self.animals = []
    
    def add_animals(self, *animals):
        for one_animal in animals:
            self.animals.append(one_animal)

    def __repr__(self):
        output = f'Cage {self.id_number}\n'
        output += '\n'.join('\t'+str(animal)
                            for animal in self.animals)
        return output
    
class NoColorsPassedError(Exception):
    pass

class Zoo:
    def __init__(self):
        self.cages = []
    
    def add_cages(self, *cages):
        for one_cage in cages:
            self.cages.append(one_cage)

    def __repr__(self):
        return '\n'.join(str(one_cage)
                         for one_cage in self.cages)

    def animals_by_color(self, *color):
        if not color:
            raise NoColorsPassedError
        
        return [one_animal
                for one_cage in self.cages
                for one_animal in one_cage.animals
                if one_animal.color == color]
    
    def animals_by_legs(self, number_of_legs):
        return [one_animal
                for one_cage in self.cages
                for one_animal in one_cage.animals
                if one_animal.number_of_legs == number_of_legs]
    
    def number_of_legs(self):
        return sum(one_animal.number_of_legs
                   for one_cage in self.cages
                   for one_animal in one_cage.animals)
    
    def transfer_animal(self, target_zoo, species):
        for one_cage in self.cages:
            for one_animal in one_cage.animals:
                if isinstance(one_animal, species):
                    one_cage.remove(one_animal)
                    target_zoo.cages[0].add_animals(one_animal)
    
    #beyond3

    def animals_by(self, **kwargs):
        print(f'{kwargs=}')
        return [one_animal
                for one_cage in self.cages
                for one_animal in one_cage.animals
                if (('color' in kwargs and one_animal.color ==kwargs['color'])
                    and
                    ('legs' in kwargs and one_animal.number_of_legs == kwargs['legs']))]




