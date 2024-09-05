import random

def create_password_generator(characters):
    '''
    Takes a series of characters as feed for password
    but returns a function as object that takes length of
    password required as input

    The inner function or closure has some of its own functionality,
    it also knows what we did when we called outer function.
    This way, it can use its variables.
    '''
    def create_password(length):
        #inner function to set the length of password required
        output =[]
        #this will be our password

        for i in range(length):
            #a loop to iterate over the length of password
            output.append(random.choice(characters))
            #adding one character at a time to the password
            #random.choice(sequence) is self-explanatory
        return ''.join(output)
        #joining items of output list as a string
    return create_password
    #returns the function as object which is then fed with length

#sample
password = create_password_generator('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!()@#$%^&*abcdefghijklmnopqrstuvwxyz')
print(password(10))
#is same as
print(create_password_generator('ADEFKLSTXYZ0156789!%^&*bcdefghnotu')(10))

'''
Everytime we call the outer function we invoke an inner function,
that inner function is linked to its caller.
Think of functions as data/objects
'''


import string

def create_password_checker(min_uppercase, min_lowercase, min_punctuation, min_digits):
    '''
    A function that takes 4 inputs as specified for password
    and returns a function object that takes the password to be
    checked as input amd returns a boolean.
    '''
    uppercase_set = set(string.ascii_uppercase)
    lowercase_set = set(string.ascii_lowercase)
    punctuation_set = set(string.punctuation)
    digits_set = set(string.digits)
    #setting each collection as a set to make it easy to check

    def check_password(password):

        if len([one_character
                for one_character in password
                if one_character in uppercase_set])< min_uppercase:
            print(f'Not enough uppercase letters, min in {min_uppercase}')
            return False
            #checks for UPPERCASE characters, one at a time
            #makes a list of all of them
            #counts the length of that list and compares with min_required
            #if less than required, then prints a prompt and returns FALSE
        
        elif len([one_character
                  for one_character in password
                  if one_character in lowercase_set])<min_lowercase:
            print(f'Not enough lowercase letters; min is {min_lowercase}')
            return False
            #same LIST comprehension as above

        elif len([one_character
                  for one_character in password
                  if one_character in punctuation_set])<min_punctuation:
            print(f'Not enough lowercase letters; min is {min_punctuation}')
            return False
            #same as above
        elif len([one_character
                  for one_character in password
                  if one_character in digits_set])<min_digits:
            print(f'Not enough lowercase letters; min is {min_digits}')
            return False
            #same as above
        else:
            return True
            #if above FAILS (means password is fine) then returns TRUE
    return check_password

#sample
check = create_password_checker(1,1,1,1)
print(check('u0Kc*&LT00'))



def getitem(index):
    '''
    Takes an index value as input
    Returns a function object that takes a data sequence
    as input and returns value at the index specified for that data
    '''
    def inner(data):
        return data[index]
    return inner

#sample
f = getitem(1)    
print(f(['sandwich','tea','salad']))
print(getitem(0)(['sandwich','tea','salad']))

def doboth(f1, f2):
    '''
    Takes two functions as input to return a function
    object that takes data as input
    and returns result of both function applied on that data'''
    def inner(data):
        return f2(f1(data))
    return inner

'''
LESSON: USE FUNCTION to remove repeatition. To be flexible.
    To have higher level of abstraction
    To be used again easily
'''

'''
More about Random module
'''
