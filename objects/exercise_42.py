'''
The idea behind INHERITANCE is to take advantage of existing functionality.
One of it, is to use existing methods, but with different functionality.

'''
'''
A subclass of DICT, it allows retrieval of values using key
with flexible input, i.e. key int(1) and key str(1) are treated as same
'''
class FlexibleDict(dict):
    '''
    Inherits from Dict, and overrides only __getitem__ method
    '''
    def __getitem__(self, key): #__getitem__ invokes the [] brackets actually
        '''
        This method receives a key, if the key is in dict, we try
        to convert it into string and an integer
        
        And pass for all ValueErrors
        '''
        try:
            if key in self: #a check for presence of key
                pass
            elif str(key) in self: #if not then try to convert key into a string
                key = str(key)
            elif int(key) in self: 
                key = int(key)
        except ValueError: #ignore if can't turn it into an integer
            pass

        return dict.__getitem__(self, key)
        #call to parent __getitem__ method either with original key or modified one
    
fd = FlexibleDict()
fd['a'] = 100
fd['b']= 200
fd['3']=300
print(fd[3])
fd['af3er']=400
print(fd['af3er'])



class StringKeyDict(dict):
    '''
    This class inherits from DICT but strictly converts
    its key into string
    '''
    def __setitem__(self, key, value):
        #it calls the __setitem__ of dict class with string key
        dict.__setitem__(self, str(key), value)

class RecentDict(dict):
    '''
    Contains a user defined number of key-value pairs
    which are determined when instances are created
    It remembers only recent pairs.
    '''
    def __init__(self, maxsize):
        super().__init__()
        #SUPER returns a proxy object on which
        #methods can be invoked
        #Typically used to invoke a method on parent class
        self.maxsize = maxsize
    
    def __setitem__(self, key, value):
        dict.__setitem__(self, str(key), value)

        if len(self) > self.maxsize:
            self.pop(list(self.keys())[0])


class FlatList(list):
    '''
    Inherits from LIST class and overrides the append method
    If the item passed is an iterable, then it adds all elements of
    the iterable on by one
    If the item passed is a single object, then it is added as such
    '''
    def append(self, new_value):
        try:
            for one_item in new_value:
                list.append(self, one_item)
        except TypeError:
            list.append(self, new_value)

f1 = FlatList()
f1.append(['a','b','c'])
f1.append(1)
f1.append('x')
print(f1)