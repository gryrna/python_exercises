'''
This is for understand purpose only

Defining this module with three variable(a,b,c)
and two functions (foo, bar)
'''

__all__ = ['a','c','bar']
#this will cause (a,c,bar) to be imported
#but the rest of b and foo won't be imported
#when used as 'from exercise_37b import *'

a = 100

b = [10, 20, 30]

c = {'a':1,'b':2, 'c':3}

def foo():
    return "Hello from foo"

def bar():
    return "Hello from bar!"


'''
Why do we check __name__?
What does this do? if __name___ =='__main__':

First, when a module is loaded, it is executed from start
to end. So, every for/print command is executed.
We use 'if' to make some code execute conditionally when loaded.

Second, __name__ variable is either __main__ which means
things are currently running in the initial, default, and top-level
namespace provided by Python.

or, __name__ is defined to be current module name.

The 'if' statement checks whether the module was run directly or
it was imported by another Python code.

In simple words, it means, ONLY execute the below code if this is
the top-level program being executed. Ignore the code when we import
the module.

So, when to use it?
When modules run their own tests when invoked directly.
When modules are run interactively.

This typically appears at the bottom of the code.
'''