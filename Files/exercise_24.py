
'''
basic setup to convert file from one format to another
Can be conversion of time, currency, encryption and so on.
'''

def reverse_lines(filename, outfilename):
    #function takes two arguments, one is input file, other is the output file
    
    with open(filename) as infile, open(outfilename, 'w') as outfile:
        #learnings: file can be iterated one line at a time
        #with can be used for two or more files
        for one_line in infile:
            outfile.write(f'{one_line.rstrip()[::-1]}\n')
            #using string.rstrip() with string slicing[::-1] to reverse it
            #rstrip() removes new line character on the right side


def encrypt(filename, text):
    #takes a text input and converts it into numerical equivalent
    #then writes that to a file
    with open(filename, 'w') as outfile:
        for one_character in text:
            outfile.write(f'{ord(one_character)}\n')
            #using built in ord() to convert into UNICODE

def decrypt(filename):
    characters = [chr(int(one_character))
                  for one_character in open(filename)
                  if one_character.strip().isdigit()]
        #if character is a digit, then convert it into an integer and finally
        #convert it into a character using built in chr() and int()
    
    return ''.join(characters)


#from a given file, creates two new files one for vowels, other for consonants.

import string

def vowel_and_consonants(infilename, vowel_filename, consonant_filename):
    with open(infilename) as infile, open(vowel_filename, 'w') as vowel_out, open(consonant_filename, 'w') as consonant_out:
        for one_line in infile:
            for one_character in one_line:
                #validation for vowels and consonants
                if one_character.lower() in 'aeiou':
                    vowel_out.write(one_character)
                elif one_character.lower() in string.ascii_lowercase:
                    consonant_out.write(one_character)


#create a file that has all the shell's name written followed by all of the usernames that use the shell

from collections import defaultdict

def shell_users(filename, outfilename):
    shells = defaultdict(list)
    #easy way to do so is to create a dict, with key being shell name
    #and values being the username(a list)
    #a dict of lists

    with open(filename) as passwd, open(outfilename, 'w') as outfile:
        for one_line in passwd:
            if one_line.startswith('#','\n'):
                #leaving all comments and new lines
                continue

            username, *fields, shell = one_line.strip().split(':')
            #splitting the line into username, other fields, and lastly, shell
            shells[shell].append(username)
            #adding to the value list, with shell being the key and username being the values(items of list)

        for shell, all_users in shells.items():
            outfile.write(f'{shell}\t{",".join(all_users)}\n')
            #writing to the output file
            #join() is used to join items of a list using a separator (comma in this case)

'''
Summary:
Files are typically opened for reading and writing.
Files can be iterated one line at a time using 'for'. This saves memory.
'with' ensures files are flushed out when done with.
JSON, CSV module for files.
Read from files into built-in Python data types is efficient and powerful.
'''