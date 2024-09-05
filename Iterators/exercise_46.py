'''
Iteration is so powerful that Python makes it easy for objects to be iterable.
For this, they need have behaviors known as Iterator Protocols

Strings, Lists and Dicts are iterable, but not INT
The iterator protocol has 3 parts (__iter__, __next__, StopIteration)

__iter__ returns an iterator
__next__ is defined on an iterator
StopIteration raises an Exception call to end Iterations

Classes can be made iterable by implementing above 3 parts.
So, what does a FOR loop do?
IT asks the object whether it is iterable by using built-in 'iter' function.
This function invokes __iter__ on the object
IF the object is iterable, it calls for 'next' built-in function.
This function invokes the __next__ on the iterator.
IF __next__ raises an Exception, the loop exits.

NOTE: Unlike C, in Python the for loop doesn't require indexes. In Python,
it is the job of the object to keep producing next item. The for loop doesn't track index.

TO make a Class iterable, do this:
    Define an __iter__ method that takes 'self' as argument and returns 'self'
    Define an __next__ method that takes 'self' as argument and should return either
        a value or raise StopIteration(a must, else its a forever loop)
'''
#sample class that prints the steps as it takes for iteration

class LoudIterator:
    def __init__(self,data):
        print('\tNow in __init__')
        self.data = data
        self.index = 0
    def __iter__(self):
        print('\tNow in __iter__')
        return self
    def __next__(self):
        print('\tNow in __next__')
        if self.index >= len(self.data):
            print(f'\tself.index {self.index} is too big, exiting')
            raise StopIteration
        value = self.data[self.index]
        self.index += 1
        print(f'\tGot value {value}, incremented index to {self.index}')
        return value

for one_item in LoudIterator('abc'):
    print(one_item)

'''
Built in Enumerate let's us get the elements of a sequence
alongwith index.
example:
    for index, letter in enumerate('abcd'):
        print(f'{index}: {letter})
'''


class MyEnumerate:
    '''
    A version of enumerate that returns a the index
    and the value at that index in form of a TUPLE'
    '''
    def __init__(self, data):
        #initializing the iteratable
        self.data = data
        self.index = 0
        #this is declared because we have to keep
        #track of the index, it is the object's duty
        #moreover, __next__ like other methods loses its
        #local scope between calls

    def __iter__(self):
        #implementing iterator protocols
        return self

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        value = (self.index, self.data[self.index])
        #I see this as the only change in iterating
        #it returns a tuple in this case
        self.index += 1
        return value

#test
s = MyEnumerate('abcd')
for item in s:
    print(item)

for item in s:
    print(item)
'''
It won't print the values for the same object 2nd time
because the iterator self.index is already at index 3

So either create the object everytime or use a MultiClass iterator
That is, use a 2nd class which will be iterator for our class

We use __iter__ on the main class, but its job is to return a new
instance of 2nd class(helper class)

Benefits:
    No need to worry about loss of iteration
    To make a class iterable, all we need to do is create a Helper class
        thus, no need to clutter main class with all the __next__ and index stuff
'''
#example
class MyEnumerateIterator_1:
    '''
    Helper class whose __init__ and __next__ looks
    the same as above but
    there is no __iter__ method
    '''
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        value = (self.index, self.data[self.index])
        self.index += 1
        return value

class MyEnumerate_1:
    '''
    Main class
    '''
    def __init__(self, data):
        #observe no index specified as not required,
        #helper class does that
        self.data = data

    def __iter__(self):
        #calls an instance of the helper class on iterable object
        return MyEnumerateIterator_1(self.data)

#test
s1 = MyEnumerate_1('abcd')
for item in s1:
    print(item)

for item in s1:
    print(item)

'''
Iteration starts with index 0 but that might not always be the case
so, we add another argument to select starting point of our iteration
'''
#sample
class MyEnumeratorIterator_2:
    def __init__(self, data, start):
        self.data = data
        self.index = start
    
    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        value = (self.index, self.data[self.index])
        self.index += 1
        return value
    
class MyEnumerate_2:
    def __init__(self, data, start = 0):
        self.data = data
        self.start = start
    
    def __iter__(self):
        return MyEnumeratorIterator_2(self.data, self.start)
#test
s2 = MyEnumerate_2('abcd',1)
for item in s2:
    print(item)


#Generator as a function instead of class
def my_enumerate(data, start=0):
    index = start
    for one_item in data:
        yield (index, one_item)
        index += 1

for item in my_enumerate('wxyz',0):
    print(item)

'''
more on ENUMERATE
'''