'''
Iterable vs Iterator
An iterable object can be put inside a for loop. It implements __iter__ method,
that returns an iterator.
An iterator is an object that implement the __next__ method

Now, in many cases, the iterable is the iterator(files)
but, some iterables produce an iterator(list, string)
'''

'''
In this, we create an iterator function, that takes a directory name as an argument
with each iteration, the generator returs a single string(one line from one file)
can use os.walk() but we ignore that

'''
import os


def all_lines(path):
    for filename in os.listdir(path):
        #os.listdir() returns a list of strings, only the filenames
        full_filename = os.path.join(path, filename)
        #for fullpath, we need to join using os.path.join
        try:
            #try because we might not have permission to open a file
            for line in open(full_filename):
                yield line
        except OSError:
            pass



#version of above that returns a tuple
def all_lines_tuple(path):
    for file_index, filename in enumerate(os.listdir(path)):
        full_filename = os.path.join(path, filename)
        try:
            for line_index, line in enumerate(open(full_filename)):
                yield (full_filename, file_index, line_index, line)
        except OSError:
            pass

#version that returns 1st line from one file, then from second file
#then 2nd line from one file, then from second file in an alternate fashion
def open_file_safely(filename):
    #modified the open function
    try:
        return open(filename)
    except OSError:
        return None

def all_lines_alt(path):
    all_files = [open_file_safely(os.path.join(path, filename))
                 for filename in os.listdir(path)]
    #a list of all the files
    
    while all_files:
        #if the directory has file
        for one_file in all_files:
            #going one by one
            if one_file is None:
                all_files.remove(one_file)
                #removes the file from list when it reaches the end
                continue
            one_line = one_file.readline()
            #reading one line at a time

            if one_line:
                yield one_line
            else:
                all_files.remove(one_file)


#version takes two arguments, a directory name and a string
#only those lines that have the string will make it to the output
#same as above except the condition
def all_lines(path, s):
    for filename in os.listdir(path):
        full_filename = os.path.join(path, filename)
        try:
            for line in open(full_filename):
                if s in line:
                    #the condition
                    yield line
        except OSError:
            pass


'''
YIELD vs RETURN
yield tells the generator to keep it going and output the value for current iteration

return tells the generator to EXIT and output the value
'''