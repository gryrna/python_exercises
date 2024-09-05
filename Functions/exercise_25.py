'''
Functions provide a number of benefits:
Avoids repetition of code.
Allows higher level of abstraction.
Wraps functionality into a package and then use that package.

Python functions are objects. They can be treated as data.

Python doesn't allow for multiple definitions of same function.
When a function is defined, it is assigned to a variable.

To have multiple definitions, in Python, we use flexible parameters
that include both *args and **kwargs.

GLOBAL -> indicates a variable must be global
NONLOCAL -> indicates a variable is local to the enclosing function

__code__ attribute contains the core of the function, it keeps a count
of the arguments and variables in the function.

We can add a default value to a parameter using, parameter_name = default_value
The default parameters comes after normal parameters.
NOTE: Never use a mutable object as default value, like a list or dict.
'''

def myxml(tagname, content='',**kwargs):
    '''
    A function to format data in XML type using string as output format
    The function can take variety of forms
    General RULE: use *args or **kwargs with a 'for' loop
    Don't use them if you are planning to call values using indexes
    To use an optional argument, set its value to some default
    Use **kwargs for name-value pairs, key is argument name, value is its value
    '''
    attrs = ''.join([f'{key}="{value}"'
                    for key, value in kwargs.items()])
    '''
    Used LIST comprehension and dict.items() on 'kwargs' DICT, in order to separate key-value pairs
    Used string format and str.join() on empty spaces to format the key-value pairs
    '''
    return f'<{tagname}> {content} {attrs}</{tagname}>'

#Sample call
myxml('food')
myxml('food', 'bar')
print(myxml('food','bar',a=1, b=2))



def copyfile(infilename, *copies):
    '''
    This take one mandatory argument that is the filename to be copied
    and, any number of additional arguments - that is the filename of copies to be made'''
    for outfilename in copies:
        #running a loop for every additional argument in 'args'
        #remember it can be called anything, e.g. 'copies' with splat operator (*copies)
        with open(outfilename,'w') as outfile:
            #using with to close the file one done
            for one_line in open(infilename):
                #iterating over each line one by one
                outfile.write(one_line)

infilename = 'Python_Workout/Files/Martix.tsv'
outfilename = 'Python_Workout/Functions/Copy1.txt'
copyfile(infilename, outfilename)


def factorial(*args):
    '''
    This takes any number of integers and multiply them by one another
    it can multiply a single char with integer but not more than one char
    NOTE: suggest a better name, as this is not a factorial function in true sense
    '''
    if not args:
        return 0
    #validation check for empty argument
    
    total = args[0]
    #initialization, plus, cases where only single integer has been passed
    for one_number in args[1:]:
        #using slicing to iterate over rest of the list except first item
        #this also prevents duplicate multiplication
        total *= one_number
        #multiplying one number at a time
    return total

#sample call
print(factorial(5))
print(factorial())
print(factorial(5,4,3))

def anyjoin(seq, glue=' '):
    '''
    Takes a sequence and jostrins the item using glue as operator
    '''
    return glue.join([str(one_item)
                      for one_item in seq])
    #using LIST comprehension to iterate over each item of 'seq'
    #also making sure that each item is a string before joining.

#sample call
print(anyjoin('gryrna', glue='*'))
print(anyjoin([1,2,3,4], glue='*'))