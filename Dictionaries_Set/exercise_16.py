#a function that outputs differnce between two dicts
#if no differnce, output is empty
#for each key-value pair the output is a dict
#that contain values as a list of values from two dicts

d1 = {'a':1, 'b':2, 'c':3}
d2 = {'a':1, 'b':2, 'c':4}

d3 = {'a':1, 'b':2, 'd':3}
d4 = {'a':1, 'b':2, 'c':4}

d5 = {'a':1, 'b':2, 'd':4}

def dictdiff(first, second):
    output = {}
    #an empty dictionary for our output

    all_keys = first.keys() | second.keys()
    #dict.keys() returns an object that has same methods as sets
    #set of all keys

    for key in all_keys:
        #check for each key in both dict
        if first.get(key) != second.get(key):
            #update output with a list of values
            output[key] = [first.get(key), second.get(key)]
    return output

print(dictdiff(d1,d5))

#using dict.update() to merge two dict
#the most rececntly merged dict's value is used

def multi_update(*args):
    output = {}
    for one_dict in args:
        output.update(one_dict)
    return output


print(multi_update(d1,d3,d4))

#whenever encountered with even-odd, try using slicing

#partition a dictionary based on output of function
#the function needs to defined separately
def partition_dict(d, f):
    output_true = {}
    output_false = {}

    for key, value in d.items():
        if f(key, value):
            output_true[key] = value
        else:
            output_false[key] = value

    return output_true, output_false

