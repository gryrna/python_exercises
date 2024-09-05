'''
Variable Scoping
Scoping refers to the visibility of variables from within the program

Python has 4 levels of scoping:
LOCAL
ENCLOSING FUNCTION (Function inside a function)
GLOBAL
BUILT-INs

In a function, all 4 levels are searched in order.
Outside a function, only GLOBAL and Built-Ins are searched

Shadowing a value: When you define a GLOBAL name identical to a Built-In
GLOBAL is searched before BUILT-IN, thus making the built-in ineffective.

LOCAL variables(inside a function) exists as long as the function does.

use global 'variable_name' to change a global variable from inside a function

Example:
def food(x):
    def stall(y):
        return x*y
    return stall

f = food(10)
print(f(20))

The result is 200.
The inner function aka closure is a function that's defined when outer function is
executed.
When we run food() it gives us stall() back. So, f is stall().
And, stall() gives x*y back. Thus, our x=10, y=20 and we get 200.
Also, stall() is a local variable inside of food()
First, Python looks for x locally, inside the function stall()
Second, Python looks for x in enclosing function food()
If not found, Python will look for x globally, and finally in built-ins

'''

def food():
    counter = 0
    #counter is local variable to food()
    def stall(y):
        nonlocal counter
        #'nonlocal' makes counter to be treated as not local to stall()
        #this means, it is local to the outer function i.e. food()
        counter += 1
        #this would lead to reference error if not made nonlocal
        return f'y = {y}, counter = {counter}'
    return stall


f = food()
#invoking food() to return stall(), this sets counter to 1
print(f(10))

for i in range(10, 100, 10):
    print(f(i))
    #printing the rest of output.


import operator

def calc(to_solve):
    '''
    A function that expects input in simple math expression in reverse Polish notation-
    operator and two numbers
    The function parses the input and returns the output
    '''
    operations = {'+': operator.add,
                  '-': operator.sub,
                  '*': operator.mul,
                  '/': operator.truediv,
                  '**': operator.pow,
                  '%': operator.mod}
    #using the operator module and listing operators as key-value pairs
    #remember, values can be any object, that includes functions

    
    op, first_s, second_s = to_solve.split()
    #unpacking the input into various parts, making a list out it
    #can also use maxsplit parameter to limit splits to three, str.split(maxsplit=2)
    #maxsplit ensures we get no error while unpacking
    first = int(first_s)
    second = int(second_s)
    #converting items into integers

    return operations[op](first, second)
    #this is DICT[key](int1, int2), like operator.add(2,3)


print(calc('** 2 3'))
#print(calc('** 2 3 5'))
#will throw an error


def calc_all(to_solve):
    '''
    An upgraded function that takes more than two numbers as input
    in a sequence format and applies the operator from left to right.
    '''
    operations = {'+': operator.add,
                  '-': operator.sub,
                  '*': operator.mul,
                  '/': operator.truediv,
                  '**': operator.pow,
                  '%': operator.mod}
    
    op, *numbers = to_solve.split()
    #unpacking into operator, and a list
    #NOTE: the splat operator * is required to tell Python
    #to expect more than one entry
    if not numbers:
        return 0
    #validation check
    output = int(numbers[0])
    #initiation plus case for single input
    for one_number in numbers[1:]:
        #iterating over rest of list using slicing
        output = operations[op](output, int(one_number))
        #same as above

    return output

#sample
print(calc_all('/ 100 5 5'))
print(calc_all('+ 3 5 7 8'))


def apply_to_each(f, seq):
    '''
    Takes a function and a sequence as input
    Applies the function on all items of sequence
    The function takes single argument like str(), int()
    '''
    return [f(one_item)
            for one_item in seq]
    #a simple LIST comprehension

print(apply_to_each(str, [1, 2, 4, 6]))
print(apply_to_each(float, [1, 2, 4, 6]))


def transform_lines(f, infilename, outfilename):
    '''
    Takes a function, alongwith input and output files.
    The function takes single argument'''
    with open(infilename) as infile, open(outfilename, 'w') as outfile:
        for one_line in infile:
            outfile.write(f(one_line))

infilename = 'Python_Workout/Files/Martix.tsv'
outfilename = 'Python_Workout/Functions/Copy1.txt'

#transform_lines(int, infilename, outfilename)
#go to check this for strings


'''
More about Operator module
'''