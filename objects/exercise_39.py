'''
People from other languages think __init__ is a constructor,
means that it creates new instances of a class. But, that's not
TRUE.

When a class is called with parameter, Python first looks for the
class, in the same manner it looks for other variables.
It finds the varaible referencing a class, which is then invoked,
and the parameter is passed to it.
The constructor method __new__ creates the new instances and returns
it to the caller of the class. Before returning it, __new__ looks for
__init__ and invokes it.

Bottom Line: __init__ is called after the object is created, but before
the object is returned.
And, __init__ adds new attributes to the object.

__init__ doesn't use return keyword. Its return doesn't matter. Once __init__
has added attributes to the new instances created by __new__ it exits.
It is job of __new__ to return the new instance to its caller.
'''

'''
#sample
Using two separate classes(Scoop, Bowl) to create a Bowl of Scoops
i.e. Smaller objects combined together to form larger object
'''

class Scoop:
    '''
    From exercise_38
    '''
    def __init__(self, flavor):
        self.flavor = flavor

class Bowl:
    '''
    Instance doesn't take a parameter,
    creates a new empty bowl(a list) with methods
    '''
    def __init__(self):
        self.scoops = []
        #creates a new empty list to mimick the empty bowl

    def add_scoops(self, *new_scoops):
        #function to add scoops to the bowl
        #takes a single item or a tuple
        for one_scoop in new_scoops:
            self.scoops.append(one_scoop)
            #using append on list object

    def __repr__(self):
        #function to return a string containing
        #an object's printed representation
        return '\n'.join(s.flavor for s in self.scoops)
        #using a Generator expression to form a string

'''
Composition is when one object contains another object
It helps in creating larger objects using smaller ones
Like a CAR using smaller objects as in Motor, Gear, Battery

So, Composition defines a HAS-A relationship.
'''

#sample
new_bowl = Bowl()
#a new instance of Bowl class(an empty bowl)
new_bowl.add_scoops(Scoop('vanilla'))
#adding one scoop to it, Scoop is instance of Scoop class
#takes Flavor as parameter
new_bowl.add_scoops(Scoop('pineapple'))
new_bowl.add_scoops(Scoop('cookie cream'), Scoop('chocolate'))
print(new_bowl)
#the return value using __repr__

'''
#sample
A Book Class has 4 attributes(title, author, price, width)
A Shelf Class let's us add books to it, has 1 parameter(width)
and 3 methods add_book and total_price, has_book
'''

class TooManyBooksOnShelfError(Exception):
    #Error class that inherits from Exception class
    pass

class Book:
    '''
    Takes 4 parameters title, author, price, width
    '''
    def __init__(self, title, author, price, width):
        #instance of Book
        self.title = title
        self.author = author
        self.price = price
        self.width = width
    
class Shelf:
    '''
    Takes width of shelf as parameter
    '''
    def __init__(self, width):
        #new instance of Shelf, also creates an empty list
        self.books = []
        self.width = width
    
    def add_books(self, *args):
        #method to add new books
        for new_book in args:
            #iteration over each book
            if self.total_width() + new_book.width > self.width:
                #validation to check empty space on Shelf
                raise TooManyBooksOnShelfError('Too many books!')
                #pass the error message as output
            self.books.append(new_book)
            #if space is there, add the book
    
    def total_price(self):
        #sums price of all books on the shelf
        return sum(one_book.price
                   for one_book in self.books)
                #a simple generator
    
    def has_book(self, title):
        #checks the presence of book on shelf
        return title in (one_book.title
                         for one_book in self.books)
    
    def total_width(self):
        #calculates sum of books' width already on shelf
        return sum(one_book.width
                   for one_book in self.books)

#sample
book1 = Book(
    title="To Kill a Mockingbird",
    author="Harper Lee",
    price=14.99,
    width=1.5
)

# Instance 2
book2 = Book(
    title="1984",
    author="George Orwell",
    price=9.99,
    width=1.2
)

# Instance 3
book3 = Book(
    title="The Great Gatsby",
    author="F. Scott Fitzgerald",
    price=12.99,
    width=1.0
)

# Instance 4
book4 = Book(
    title="Moby-Dick",
    author="Herman Melville",
    price=18.50,
    width=1.8
)

#Instance of shelf with width
shelf1 = Shelf(5)

shelf1.add_books(book1,book2,book3)
print(shelf1.has_book('1984'))
print(shelf1.total_width())
print(shelf1.total_price())

# shelf1.add_books(book4)
#must throw an error

'''
Python only has one tool, 'Attribute'
Whenever there is a.b in code, it means 'b' is attribute of 'a'
i.e. 'b' references an object 'a'

NOTE: Unlike, C# and JAVA, we don't declare attributes, we must
actually create and assign them at runtime
'''

'''
The 'self' (first parameter) refers to the instance. Attributes added to 'self'
sticks around after the method returns. Thus, it is natural to assign a bunch of
attributes to self in __init__
'''  
