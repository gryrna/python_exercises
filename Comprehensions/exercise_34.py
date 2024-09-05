'''
Python's basic data structures can be used to solve
a variety of problems
It is daunting to select appropriate DS which is
usually a combination of two or more
NOTE: A comprehension with {} is a set
    {} with : is a dict
    [] is a list
'''
def get_sv(filename):
    '''
    Takes a file and returns a set of all words
    that are supervocalic(has all vowels)
    '''
    vowel = {'a','e','i','o','u'}
    #set of all vowels
    return {word.strip()
            #strip removes all empty spaces
            for word in open(filename)
            #iteration over each word, each line has only one word
            if vowel < set(word.lower())}
            #for sets '<' returns True if set on left is subset of right
            #dict and set use {} when created new

#sample
filename = 'Python_Workout/Comprehensions/words.txt'
count = 0
for item in (get_sv(filename)):
    print(item, end='\n')
    count+=1
print(count)
#counting total number of words

def different_shells(filename):
    '''
    For a unix etc/password file
    outputs the different shells
    '''
    return {one_line.split(':')[-1].strip()
            for one_line in open(filename)
            if not one_line.startswith(('\n','#'))
            #condition to remove comments and empty lines
            }

def word_lengths(filename):
    '''
    For a file, counts the length of words
    and returns a set of length of those words
    '''
    return {len(one_word)
            #expression
            for one_line in open(filename)
            #1st iteration
            for one_word in one_line.split()}
            #2nd iteration, if line has more than one word

#sample
print(word_lengths(filename))
#the file has max word of length 24

import string

def letters_in_names(list_of_names):
    '''
    Returns a list whose elements are strings
    and also finds which letters are used in those strings
    '''
    return {one_letter
            #expression: we want one letter to form a set
            for one_letter in ''.join(list_of_names).lower()
            #iterating over whole file
            if one_letter in string.ascii_letters}
#sample
names = names = [
    "Alice Johnson",
    "Charlie Brown",
    "Diana Prince",
    "Frank White",
    "Grace Adams",
    "Ivy Taylor",
    "Jack Wilson",
    "Liam Martinez",
    "Mia Robinson",
    "Olivia Young",
    "Paul King",
    "Rachel Lee",
    "Samuel Walker",
    "Ulysses Harris",
    "Vera Allen",
    "Xena Wright",
    "Yara Hill",
    ]

print(letters_in_names(names))