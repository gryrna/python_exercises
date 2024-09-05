'''
In python, a function can take another function
as argument because it is an object only.
'''

def hex_to_dec(hexstring):
    '''
    A sample function that convers hex to decimal
    '''
    if hexstring.startswith('0x'):
        hexstring = hexstring[2:]
        #actually hexstring is only the part after 0x
    decimal_value = int(hexstring, 16)
    #int(string, 16) means input is in base-16
    return decimal_value

def transform_values(func, a_dict):
    '''
    Takes a function and a dictionary
    Applies that function to values of dictionary
    and returns a new dictionary
    '''
    return {key: func(value)
            #expression format we want
            for key, value in a_dict.items()}
            #separating tuple one at a time
            #iteration

#sample
dict = {
    'a': '0x61',
    'b': '0x62',
    'c': '0x63',
    'd': '0x64',
    'e': '0x65',
    'f': '0x66',
    'g': '0x67',
    'h': '0x68',
    'i': '0x69',
    'j': '0x6A',
    'k': '0x6B',
    'l': '0x6C',
    'm': '0x6D',
    'n': '0x6E',
    'o': '0x6F',
    'p': '0x70',
    'q': '0x71',
    'r': '0x72',
    's': '0x73',
    't': '0x74'
    }

print(transform_values(hex_to_dec,dict))


def tranform_values2(func1, func2, a_dcit):
    '''
    Does the same as above
    but takes two functions
    applies function1 to value
    if function2(key,value) returns True
    '''
    return {key: func1(value)
            for key, value in a_dcit.items()
            if func2(key, value)}