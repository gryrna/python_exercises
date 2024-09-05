'''
Import statement looks for module in a number of directories.
The directories are defined in a list of strings.
LIST is called sys.path

If python finds a file in these directories, it stops looking
further.

A way to modify to sys.path is by including enviroment variable
PYTHONPATH or by creating files with .pth suffix in Python's installation
site-packages directory.

So, import does 2 things: loads the module and defines a new variable.

For cases when modules import modules, and some of them are same,
Python will load the module the first time, but only define variable
the second time.
Example: pandas and scipy both import numpy. Python will load numpy from pandas
and for scipy only define a variable.

This is done via a DICT defined in sys called sys.modules
Key: name of module
Value: module objects
'''


'''
#sample
Defining a generic function to be used in variety of programs
Call it 'menu' module
This is an example of dispatch table
'''

def menu(**options):
    '''
    Takes any number of key-value pairs as arguments.
    The value should be a callable(i.e. a function)
    
    When the function is invoked, the user is asked to
    enter some input.
    If input matches a string of one of the keyword arguments
    the function associated with it is invoked
    '''
    while True:
        option_string = '/'.join(sorted(options))
        choice = input(f'Enter an option ({option_string}): ')
        if choice in options:
            return options[choice]()
        
        print('Not a valid option')
