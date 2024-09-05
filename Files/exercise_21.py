#longest word per file
#working across multiple files

#2 functions, one to track longest_word in a file
#other to keep a record of longest_word in all files in directory

#we will use books directory for this test

'''
To list files in a directory, we have 2 common ways
First: use os.listdir
    Pros: Easy to work with and provides a list of files in a directory.
    Cons: Lists files without directory name, so we have to add directory name
        using os.path.join() which works across platforms.
        Can't filter filenames by pattern. It lists everyfile including hidden.
        So, not good, if we only want .jpeg or .txt files
Second: use glob.glob
    Pros: Let's us use Patterns. Returns a list of strings.
        Each string is full path to filename.
        example: filename = glob.glob(f'{dirname}/*.conf'})
            to only output configuration files
Third: use pathlib.Path
    Pros: Creates a path object that represents a file or directory.
        Once created, many things can be done with it like using iterdir()
        example: p = pathlib.Path('dirname')    
            for one_file in p.iterdir():
                print(one_file)
        each Iteration returns a 'path' not a string.
        
        Can use glob() to list files matching a pattern
        example: for one_file in p.glob('*.conf'):
                    print(one_file)
                    
'''

import os

def longest_word(filename):
    longest_word = ''
    for one_line in open(filename):
        for one_word in one_line.split():
            if len(one_word) > len(longest_word):
                longest_word = one_word
    return longest_word

# file = 'Python_Workout/Files/books/43-0.txt'

# print(longest_word(file))

def find_all_longest_words(dirname):
    #for a given directory, returns a dict with key as filename,
    #  and values are longest word in that file

    return {filename: longest_word(os.path.join(dirname, filename))
            for filename in os.listdir(dirname)
            if os.path.isfile(os.path.join(dirname, filename))}
            #using dict comprehension to create a dict by iterating over a list of filenames
            #dict will iterate of list of files in the directory
            #add files to the variable 'filename'
            #for each file, run 'longest_word' function
            #the dict will make key-value pair of filename and longest word


# print(find_all_longest_words('Python_Workout/Files/books'))

'''
Whenever it comes to transforming one collection of inputs
into a collection of outputs, always use comprehensions,
most commonly List comprehensions, but set and dict are also common

'''

'''
About OS.path
and, os.join
from File and Directory Access section'''


#example: use md5 hash and print md5 hash for all files in a directory

import glob
import hashlib

def md5_files(dirname):
    output = {}

    for one_filename in glob.glob(f'{dirname}/*'):
        try:
            m = hashlib.md5()
            m.update(one_filename.encode())
            output[one_filename]=m.hexdigest()
        except:
            pass
    return output

'''
About hashlib
About glob'''

# print(md5_files('Python_Workout/Files/books'))

#example: show all files in a directory, and when it was last modified

import arrow
def mod_time(dirname):
    output = {}

    for one_filename in glob.glob(f'{dirname}/*'):
        try:
            mod_time = os.stat(one_filename).st_mtime
            output[one_filename] = (arrow.now() - arrow.get(1503636889)).days
        except:
            pass
    return output

# print(mod_time('Python_Workout/Files/books'))

'''
About arrow module

'''

#example: read from a log file and summarize it using counts

from collections import Counter

def response_count(filename):
    output = Counter()

    for one_line in open(filename):
        output[one_line.split()[8]] += 1

    return output

print(response_count('Python_Workout/Files/books/http_server_log.txt'))

'''
understanding File structure is of utmost importance while dealing with files
'''


