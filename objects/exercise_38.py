'''
Idea behind OOPS is simple: Instead of defining our functions
in one part of the code and the data on which they work in a 
separate part of code, we define them together

In OOPS, each noun is an object
Each object has a type(class) and
we use functions(methods) on such object

OOPS allows:
    Defining our own types, which inturn allows us
    to think at a higher level of abstraction.
    Easy planning and maintenace.
    Hierarchies of classes with each child inheriting
    from parent, this reduces amount of code.

In Python, everything is an object. Types like STR, DICT
are classes that have methods.

Each class represent only ONE TYPE of object and its behavior.

'''

'''
#sample
Define a SCOOP class to represent single scoop of ice cream
Each scoop has a single attribute(variable) called TASTE
'''

class Scoop:
    '''
    Create one scoop of defined TASTE
    Scoop(taste)'''
    #The keyword 'class' is used to create a TYPE
    def __init__(self, taste):
        #function invoked automatically when a new instance is created
        #invoked after new instance is created but before it has been returned to whoever invoked it
        #in this case Scoop('flavor')
        #now the new object is passed to __init__ method in 'self'(the first parameter) and alongwith other parameters

        self.flavor = taste
        #the FLAVOR attribute is initialized when an instance is created
        #the self.attribute_name is used to pass attribute to the new instance
        #here it sets the 'flavor' attribute to the value in parameter 'taste'

def create_scoop():
    '''
    This function creates three instances of SCOOP class
    each having different taste.
    '''
    scoops = [ Scoop(taste)
              for taste in ['Chocolate','Vanilla','Pineapple','American nut']
            ]
    #a list of instances of SCOOP class
    #3 scoop objects
    
    for scoop in scoops:
        #iteration over each scoop object
        print(scoop.flavor)
        #calling attribute of the object using dot(.) notation
        #and printing its value

#test
create_scoop()

class Beverage:
    '''
    Creates a Beverage type object that has a name, and suggested temp
    to serve
    '''
    def __init__(myself, known_as, serve_at):
        #First parameter can be called anything
        myself.name = known_as
        myself.temp = serve_at
        #values in the parameters 'known_as' and 'serve_at' are fed to attributes 'name' and 'temp'

#sample
#creating an instance of class Beverage
apple_juice = Beverage('apple juice',20)
milk = Beverage('milk', 4)
beer = Beverage('fruit beer', 0)
#calling an attribute of the object
print(apple_juice.temp)
print(beer.name)


class Beverage:
    '''
    Like above but has a default temp value
    So, if not specified, it will take it as 75
    Plus, it also overrides the above class so Python
    won't show it
    '''
    def __init__(self, name, temp=75):
        self.name = name
        self.temp = temp

#sample
coffee = Beverage('coffee')
print(coffee.temp)
tea = Beverage('tea', 90)
print(tea.temp)


class Logfile:
    '''
    LogFile class expects a filename to be initialized
    '''
    def __init__(self, filename):
        self.file = open(filename, 'w')
        #opens the filename for writing

#sample
filename = 'Python_Workout/objects/Copy1.txt'
#creating an instance
sample = Logfile(filename)
#using that instance's file attribute to write to the sample file
for i in range(10):
    i = str(i)
    sample.file.write(i)

'''
The first parameter in every method is traditionally called SELF
You can call it anything.
'''