'''
CSV files
Each record is a separate line and fields are separated by comma(or another delimiter like : ; \t)

For more advanced way to handle CSV files, use PANDAS
'''

import csv

def passwd_to_csv(passwd_filename, csv_filename):

    with open(passwd_filename) as passwd, open(csv_filename, 'w') as output:
        #using WITH to open two files and both will be closed by the end of program
        infile = csv.reader(passwd, delimiter=':')
        #input has ':' as delimiter, need to specify it, else it looks for comma
        outfile = csv.writer(output, delimiter='\t')
        #the output uses TAB as delimiter
        
        for record in infile:
            if len(record) > 1:
                #validation to weed out comments, and malformed lines
                #can also use str.startswith() to weed out comments only
                outfile.writerow((record[0], record[2]))
                #writes username and user id

passwd_file = 'Python_Workout/Files/passwd.txt'

'''
More about CSV module

Example:
with open('sample.csv', 'w') as  file:      <- open csv file using with
    o = csv.writer(file)                    <- creates a csv.writer object, that wraps file-like object 
    o.writerow(range(5))                    <- this writes to the csv file, creating a record(one line)
    o.writerow(['a','b','c','d','e'])
    
'''

def passwd_to_csv(passwd_filename, csv_filename, fields_to_pass='1 2', delimiter='\t'):
    #user can input space-separated list of integers, that indicates which fields to choose
    #user can choose own delimiter
    fields_to_pass = [int(one_item)
                      for one_item in fields_to_pass]
    
    with open(passwd_filename) as passwd, open(csv_filename,'w') as output:
        infile = csv.reader(passwd, delimiter=':')
        outfile = csv.writer(output, delimiter=delimiter)

        for record in infile:
            if len(record) > 1:
                fields = [one_field
                          for index, one_field in enumerate(record)
                          if index in fields_to_pass]
                
                outfile.writerow(*fields)

def dict_to_csv(dict, csv_filename):
    #writes a dictionary to a csv file
    with open(csv_filename, 'w') as output:
        outfile = csv.writer(output, delimiter='\t')
        #same setup as above, open in write mode, choose a delimiter

        for key, value in dict.items():
            outfile.writerow([key, value, type(value)])
            #read from dictionary and write to csv

import random

def random_csv(csv_filename):
    #write to a csv file 10 lines containing 1o random integers

    with open(csv_filename, 'w') as output:
        outfile = csv.writer(output)

        for i in range(10):
            output = []
            for j in range(10):
                output.append(random.randint(10, 100))

            outfile.writerow(output)

    for one_line in open(csv_filename):
        #read from that CSV and print out sum and mean of each line
        numbers = [int(one_item)
                   for one_item in one_line.split(',')]

        print(f'sum = {sum(numbers)}, mean = {sum(numbers)/len(numbers)}')

random_csv('Python_Workout/Files/output.csv')





