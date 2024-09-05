'''
About JSON
Popular file format for data exchange across web and APIs

Python has built-in JSON module
json.load() reads a JSON-encoded string and returns a combination of Python objects

JSON, like XML is a data representation. To make use of them in Python, we convert them to
Python formatted strings and then convert them back to original form.

'''

'''
For this exercise, we have test data from high school. They are in Scores directory
Each file is for scores of one class
'''

import json
import glob
import csv

def print_scores(dirname):
    scores = {}
    #will be a dict of dicts, first level will be the filename
    #second level will be subjects
    #the dict values will be a list of scores


    for filename in glob.glob(f'{dirname}/*.json'):
        #we can use os.listdir and then filter only JSON files
        #or, use glob to match a pattern for files ending with .JSON
        #here glob returns files havning .json extension in the 'scores' directory
        scores[filename] = {}
        #further creating an empty dict with filename as key

        with open(filename) as infile:
            for result in json.load(infile):
                #json.load read the single array from the infile
                #returns a Python list of dicts(that can be iterated)
                #use json.loads to multiple arrays from a file
                
                #each 'result' is a dict
                for subject, score in result.items():
                    #taking individual dict at a time
                    scores[filename].setdefault(subject, [])
                    #using dict.setdefault(k,v) that means, if 'k' doesn't exist in dict, 
                    # creat it and add value 'd'
                    scores[filename][subject].append(score)
                    #this is at second level of dict
                    #we don't know how many tests there are, so will take all resutls in a list
    
    for one_class in scores:
        #once the scores are created, we iterate over them to summarize
        #this function prints the output on the screen
        print(one_class)
        for subject, subject_scores in scores[one_class].items():
            #again using dict.items() to return key-value pairs
            min_score = min(subject_scores)
            max_score = max(subject_scores)
            average_score = (sum(subject_scores)/
                             len(subject_scores))
            
            print(subject)
            print(f'\t min {min_score}')
            print(f'\t max {max_score}')
            print(f'\t mean {average_score}')


print_scores('Python_Workout/Files/json-files/scores')

#example: CSV to JSON, JSON will have list of tuples, each tuple is one line from CSV

def csv_to_json(filename):
    output = []

    for one_line in open(filename):
        if one_line.startswith('#'):
            continue
        if one_line.strip().startswith('\n'):
            continue

        output.append(tuple(one_line.split(':')))

    return json.dumps(output)

print(csv_to_json('Python_Workout/Files/passwd.txt'))

#example: turn CSV to Dict
def json_passwd_dict(filename):
    fields = ['username', 'password', 'uid', 'gid', 'name', 'homedir', 'shell']

    output = []
    for one_line in open(filename):
        if one_line.startswith('#'):
            continue
        if one_line.strip().startswith('\n'):
            continue

        output.append(dict(zip(fields, one_line.split(':'))))

    return json.dumps(output)


#example: read all files from a directory, get size of the file, and last modified
#then print it out

import os

def write_file_info(dirname, outputfile):
    output = []
    for one_filename in glob.glob(f'{dirname}/*'):
        if not os.path.isfile(one_filename):
            continue

        try:
            output.append({'filename': one_filename,
                           'size': os.stat(one_filename).st_size,
                           'mtime': os.stat(one_filename).st_mtime})
        except:
            print(f'Error reading {one_filename}; skipping')

    return json.dump(output, open(outputfile, 'w'))


def read_file_info(filename):
    output = {}

    file_info = json.load(filename)

    return output


