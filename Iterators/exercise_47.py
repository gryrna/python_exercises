'''
A Helper iterator class(CircleIterator) and Main class(Circle)
that works with 2 arguments(a sequence, a number)
It returns elements the defined number of times.
It returns repeating elements if the sequence
has less number than defined
'''
class CircleIterator:
    def __init__(self, data, max_times):
        self.data = data
        self.max_times = max_times
        #this tells how many iterations we need
        self.index = 0
    
    def __next__(self):
        if self.index >= self.max_times:
            raise StopIteration
        value = self.data[self.index % len(self.data)]
        #the % operator does the trick with index
        #it returns integer remainder
        #when index is higher than length of sequence
        #it gives the remainder, that moves it back to 0,1,2...
        self.index += 1
        return value
    
class Circle:
    def __init__(self, data, max_times):
        #takes 2 arguments
        self.data = data
        self.max_times = max_times
    
    def __iter__(self):
        #invokes helper class
        return CircleIterator(self.data, self.max_times)

#test
print(list(Circle('abc',5)))

#instead of helper, we can inherit from main class

class CircleIterator_1:
    '''
    Main class
    '''
    def __init__(self, data, max_times):
        self.data = data
        self.max_times = max_times
        self.index = 0
    def __next__(self):
        if self.index >= self.max_times:
            raise StopIteration
        
        iterated_data = getattr(self, self.returns)
        #from original data, generate a filtered data, using attributes required
        value = iterated_data[self.index % len(iterated_data)]
        self.index += 1
        return value
    
    def __iter__(self):
        return type(self)(self.data, self.max_times)

class Circle_1(CircleIterator_1):
    def __init__(self, data, max_times):
        super().__init__(data, max_times)
        self.returns = 'data'
        #a list of attribute names that should be returned


#defining as a generator function
def circle(data, max_times):
    for index in range(max_times):
        yield data[index % len(data)]


#an implementation of built-in Range
class MyRange:
    def __init__(self, first, second=None, step=1):
        if second is None:
            self.current = 0
            self.stop = first
        else:
            self.current = first
            self.stop = second
        self.step = step

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current >= self.stop:
            raise StopIteration
        value = self.current
        self.current += self.step
        
        return value