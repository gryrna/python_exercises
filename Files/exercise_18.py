'''
important modules
OS
input output(io) from generic OS services
glob from File and Directory access
hashlib from Cryptographic services
csv from file services
json from internet data handling


Files are data structures that can be read and written to.
File like objects are all iterable.

'With' puts the object in Context Manager, for a file
it ensures that the file is flushed and closed by the end
of its functioning

'Context Manger' makes object work in 'with' statements

'''

#a function to print final line of a file

def get_final_line(filename):
    final_line = ''
    with open(filename) as f:
        for current_line in f:
            final_line = current_line
    return final_line

#f = open('Python_Workout/Files/myshells.txt')
'''open function returns a number of different object such as TextIOWrapper, BufferedReader
open(filename) the filename is a string representing Filename or Relative File path
open(filename, r) or open(filename, rb) -> r for characters, rb for characters by byte
instead of creating a separate variable, we can do that in the function

but this leaves the file open and we don't want that. So to close the file once it is done with,
we use the 'with' construct.

'''
f = 'Python_Workout/Files/myshells.txt'
print(get_final_line(f))

'''
More on Opening Files

When we open files using open(filename, r), we open in read mode
and python expects a UTF-8 characted encoding
This is not true in case of Binary File like PDf, JPEGs
this is why we use binary mode or byte mode, open(filename, rb)

for byte mode, we don't read lines, as there is none, rather we read bytes
using the file.read(bytes) method.
So, for last line, we will get 0 bytes.

'''

#function to add the product of two columns
def sum_mult_columns(filename):
    total = 0
    
    for one_line in open(filename):
        fields = one_line.split()
        #split() returns a list of substrings

        #limiting to 2 columns only
        if len(fields)!=2:
            continue
        
        first, second = fields
        #assigning list items to first and second

        if not first.isdigit():
            continue
        if not second.isdigit():
            continue
        #check for interger values

        total += int(first)*int(second)
        #final sum
    
    return total

print(sum_mult_columns('Python_Workout/Files/Martix.tsv'))


#function to count total vowels in a filename
def count_vowels(filename):
    output = dict.fromkeys('aeiou', 0)
    #fromkeys() creates dict from an iterable as key, and default values

    for one_line in open(filename):
        #iterate over the file and then each line in that file
        for one_character in one_line.lower():
            if one_character in output:
                output[one_character] += 1

    return output

print(count_vowels('Python_Workout/Files/passwd-vowels.txt'))

