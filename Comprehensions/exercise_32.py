'''
DICTs and Comprehensions is a powerful combination

Think over what you want in return, an object or only the value.
If you want object, go for comprehension
If you want value, choose for loop
'''
def flipped_dict(a_dict):
    '''
    Takes a dict and flips it.
    Values becomes keys and keys become values

    2 ways
    '''
    # return {value: key 
    #         #Format in which we want our list
    #         for key, value in a_dict.items()}
    #         #simple iteration over dict tuples
    
    return {a_dict[key]: key for key in a_dict}


#sample
d={'aBcDe': 67, 'FgHij': 23, 'KlMno': 84, 'pQrSt': 12, 'UvWxY': 45}
print(flipped_dict(d))

def vowel_count(word):
    '''
    Takes a sequence and counts the number of vowels

    2 ways to do it
    but we want return value so a for loop
    '''
    total = 0
    for one_letter in word.lower():
        if one_letter in 'aeiou':
            total+=1
    return total

    # return len([one_letter
    #             #expression
    #         for one_letter in word.lower()
    #         #iteration
    #         if one_letter in 'aeiou'])
    #         #condition
    #         #returns a list whose len is given as output

#sample
word = 'education authorise unobtrusive simultaneous precautious sequoia '
print(vowel_count(word))


def word_vowels(s):
    '''
    Takes a sequence and returns number of vowels for
    each word in form of dict
    Want an object, so we go for comprehension
    '''
    return {one_word: vowel_count(one_word)
            for one_word in s.split()}
            #using the above function
            #split is used to separate words based on spaces

#sample
print(word_vowels(word))


import glob, os

def file_info(dirname):
    '''
    Takes a dict whose keys are filenames
    and values are length of files
    '''
    return {one_filename: os.stat(one_filename).st_size
            #dict format for the result
            for one_filename in glob.glob(f'{dirname}/*')
            #iteration over each file in directory
            if os.path.isfile(one_filename)}
            #check if the item is a file
            

def read_config(filename):
    '''
    Takes a file that has lines that look line name=value
    and returns a dict with name,value pairs
    '''
    return {one_line.split('=')[0]: one_line.split('=')[1].strip()
            #the strip() removes empty spaces from both sides
            for one_line in open(filename)}
            #iteration

file= 'Python_Workout/Comprehensions/key,value.txt'
print(read_config(file))

''' 
os.stat(filename) returns os.stat_result object
This object has many attributes
st_size <- gives size of file
st_mode <- gives file mode (permission, file type)
st_mtime <- gives last time modified
'''

'''
glob.glob() is used to find all the pathnames matching a pattern
'''
'''
os.path() provides a set of functions to interact with and manipulate file
os.path.join('folder','subfolder','filename') <- joins one or more path components into a single path
os.path.isfile('filename') <- checks if a specified path is a file
'''