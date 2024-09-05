'''
Python comes with itertools module to make iterators easily.
'''
import os

def mychain(*args):
    '''
    Takes any number of iterables and outputs their items one at a time
    '''
    for arg in args:
        for item in arg:
            yield item

[print(item)
    for item in (mychain('abc',[1,2,3],{'a':1,'b':2}))]



def myzip(*args):
    '''
    Version of zip
    takes a iterables and returns tuples taken from those iterable's element
    '''
    for i in range(len(min(args, key=len))):
        #min(args, key=len) finds the shortest iterable in args based on length
        #len of shortest is used for iteration
        yield tuple(one_arg[i]
                    for one_arg in args)

#test
lists = [[1, 2, 3], ['a', 'b', 'c', 'd'], [True, False]]
for item in myzip(*lists):
    print(item)
#be mindful of splat operator in argument


#another version from previous exercise
def all_lines(path):
    return mychain(*(open(os.path.join(path, filename))
                     for filename in os.listdir(path)
                     if os.path.isfile(os.path.join(path, filename))))

#another version of range from exercise_48
def myrange(first, second=None, step=1):
    if second is None:
        current = 0
        stop = first
    else:
        current = first
        stop = second
    while current < stop:
        yield current
        current += step

'''
That's all folk!
'''
