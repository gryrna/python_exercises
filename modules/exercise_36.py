'''
A step towards DRY(don't repeat yourself)
use functions to avoid repeatition within a program
Use Modules(library) to avoid the same within multiple programs
A module can have any Python object, from simple data structures
to functions to classes.
The only question is whether you want to share it across
multiple programs?

Modules are Python's way of creating namespaces
Each file(module) has its own namespace, to ensure no
conflict between choosen variable names and functions

Modules are available on Python Package Index(pypi.org)
Visit awesome-python.com that lists only stable and maintained
packages

One of the namespaces that comes with Python is 'builtins'

Import defines a new variable that references a module
Python tries to locate a file that matches the variable name
either module_name.py or module_name.pyc
It looks for matching files in a number of directories,
visible in sys.path
Python loads the first match it encounters

Once a module is imported, all names defined in file's
global scope are available as attributes via module object

You can load the attribute by using 'from module_name import attribute_name'

NOTE: Avoid using 'from module_name import *'
    This will load the 'module' into memory and will take all attributes from
    the module and define them as global variables in the current namespace.
    Further, not all names from 'module' will be imported with import *
    Names with _ will be ignored.
    However, using 'from module_name import attribute' imports everything
    including __all__

'''

'''
#sample
Defining sales tax from a country where tax depends upon
state of purchase
Also, tax is a function of Percentage_hour of the day
So, we will make a package out of it and use it in other
examples
The calculate_tax function finds the tax
'''
RATES = {
    'Chico': 0.5,
    'Groucho': 0.7,
    'Harpo': 0.5,
    'Zeppo': 0.4
}

def time_percentage(hour):
    '''
    Gives back %age of the day that has passed based on 1 argument
    '''
    return hour/24

def calculate_tax(amount, state, hour):
    '''
    Takes 3 arguments and returns the tax owned to state
    '''
    return amount + (amount * RATES[state] * time_percentage(hour))


'''
#sample
Defining income tax as per brackets
'''
brackets = [
    {'start':0, 'end': 1000, 'tax':0},
    {'start':1000, 'end': 10000, 'tax':.1},
    {'start':10000, 'end': 20000, 'tax':.2},
    {'start':20000, 'end': 1000000000, 'tax':.5}
]

def tax_brackets(amount, brackets):
    '''
    Takes amount and a Brackets dict to return tax owed
    '''
    tax_owed = 0

    for one_bracket in brackets:
        #iterate for each tax bracket
        if amount < one_bracket['start']:
            continue
        #if amount doesn't fall in bracket, then stop

        taxed_amount = min(amount, one_bracket['end'])
        taxed_amount -= one_bracket['start']
        #amount to be taxed

        tax_owed += taxed_amount * one_bracket['tax']
        #final tax

    return tax_owed

'''
#sample
Given a string, outputs a dict indicating how many
characters provide True to each function listed below
'''
def analyze_strings(s):
    output = {
        'isdigit': 0,
        'isalpha': 0,
        'isspace': 0
    }

    for one_character in s:
        #iterating each character in the string
        for methodname in output:
            #applying each method on the character in string
            if getattr(one_character, methodname)():
                output[methodname] += 1

    return output


def fromkeys_func(s, func):
    '''
    Takes a sequence and invokes a function
    on each item
    The result is a dictionary with key being the item
    value being func(item)
    '''
    output = {}
    for one_item in s:
        output[one_item] = func(one_item)
    return output

