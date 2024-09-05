#summing anything

'''
While taking any number of arguments,
the important part is the splat * operator.
So we can use *args, or *items, or just anything with *

It produces a tuple.
'''

def mysum(*args):
    #check whether the argument is empty or not
    #can't work with empty tuple
    if not args:
        return None
    
    #assign first item to output to define output type(int, string, ...)
    output = args[0]
    #iterate over rest of the tuple
    for item in args[1:]:
        output += item
    
    return output

print(mysum(1,2))
print(mysum([1,2,3],[4,5,6]))
print(mysum('a','b','c'))

#another example of dynamic function

def sum_bigger_than(threshold, *args):
    if not args:
        return None
    output = 0
    for item in args:
        if item > threshold:
            output += item
    return output

print(sum_bigger_than(10,5,20,6,30))

#another example of dynamic function with a check
def sum_numeric(*items):
    #sum all items assuming they are numeric
    #if they aren't, skip it
    output = 0
    for item in items:
        try:
            output += int(item)
        except ValueError:
            pass
    return output

print(sum_numeric(10.20,'a',40,30))

#a function that returns a combine dictionary
def combine_dicts(*args):
    """Return a dict, the result of combining all
elements of args (which should be dicts).  If a key
occurs in more than one, then the value should be a list
containing all values from the arguments.
"""
    output = {}

    for d in args:
        for key, value in d.items():
            if key in output:
                try:
                    output[key].append(value)
                except AttributeError:
                    output[key] = [output[key], value]
            else:
                output[key] = value

    return output