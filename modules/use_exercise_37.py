from exercise_37 import menu

#let's define a few functions
def func_a():
    return 'A'

def func_b():
    return 'B'

#create an object using menu
return_value = menu(a=func_a,b=func_b)

'''
what's happening?
we invoked the menu() with key,value pairs, stored
the result in 'return_value'
when user enters a choice, the corresponding value
which is a callable is triggere
'''

print(f'Result is {return_value}')

from exercise_37b import *
# this will ignore names starting with _
# only items listed in __all__ are imported

print(c)
print(b)
# gives an error because not imported

from exercise_37b import b
#using specific call works always
print(b)

