'''
About 'with' and 'Context Managers'

'With' is general Python Construct known as a Context manager.

Use 'with' for an object and a variable to which you want to assign the object
Object must know how to work in context manager. This is done using __enter__() method
The value returned by this method is assigned to the 'as' variable at the end of 'with' line
At the end, the __exit__() method is used to restore the object back to original state.

Check 'Python Language Reference' section for more details.
'''

#word count
#a function that counts the characters, words, lines that a file contains

def wordcount(filename):

    counts = {'characters': 0,
              'words': 0,
              'lines': 0}
    #initiating an empty dict with starting values as 0
    unique_words = set()
    #for finding unique valies, as told, use SET not LIST

    for one_line in open(filename):
        counts['lines'] += 1
        #easy part, while iterating over each line just add one to count
        counts['characters'] += len(one_line)
        #again, while iterating, also count len of each line and add that to characters count
        counts['words'] += len(one_line.split())
        #while iterating over a line, create a list of words using split on spaces, 
        # add count the length of list, that our count of words

        unique_words.update(one_line.split())
        #update the empty set with words formed by list.
    
    counts['unique words'] = len(unique_words)
    #for unique words, simply use len on set
    for key, value in counts.items():
        print(f'{key}: {value}')
        #the output for each item of the dictionary

file = 'Python_Workout/Files/wcfile.txt'
#wordcount(file)

#example: counting words frequencies for user entered words in a user entered filename

def count_certain_words():
    s = input('Enter filename, then words you want to count: ').strip()

    if not s:
        return None
    
    filename, *words = s.split()
    #separating filename and words from list
    #keeping first item as filename and rest as words

    counts = dict.fromkeys(words, 0)
    #words is a list, and is iterable, default value is 0
    
    for one_line in open(filename):
        #iterating over each line ones
        for one_word in one_line.split():
            #the split() makes list of words, not using it will return characters
            if one_word in counts:
                counts[one_word] += 1

    return counts

# print(count_certain_words())

#function to create a dict with key=filename on system and value=size of those files

import glob
import os

def file_size(dirname):
    counts = {one_filename: os.stat(one_filename).st_size
              for one_filename in glob.glob(f'{dirname}/*')
              if os.path.isfile(one_filename)}
    return counts

print(file_size('Python_Workout/Files'))


'''
Learn to use 'OS'
'''
