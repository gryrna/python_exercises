import time
import os

'''
A generator function, that takes an iterable as argument
for each iteration, the generator returns a two-element tuple
The first element is seconds past previous iteration
The second element is item from passed argument
'''
'''
Unlike a function who is invoked multiple times,
and each time gets local variable set
The generator is invoked once, so it keeps
local variable memorized for iterations
'''
def elapsed_since(data):
    last_time = None
    #0 at start of program

    for item in data:
        current_time = time.perf_counter()
        #returns number of seconds since the program started
        delta = current_time - (last_time or current_time)
        #calculates time difference btw last time and now
        last_time = time.perf_counter()

        yield (delta, item)

print(list(elapsed_since('abcd')))


#min_wait is for time that must elapse before next iteration
def elapsed_since_1(data, min_wait):
    last_time = None
    for item in data:
        current_time = time.perf_counter()
        delta = current_time - (last_time or current_time)

        if delta < min_wait:
            #validation check, sleep for remaining time
            time.sleep(min_wait - delta)
        
        last_time = time.perf_counter()
        yield (delta, item)

# print(list(elapsed_since_1('abcd',1)))

#gives filee usage timings, the modified, created and accessed
def file_usage_timing(dirname):
    for one_filename in os.listdir(dirname):
        #creating a list of files in directory
        full_filename = os.path.join(dirname, one_filename)
        #full path for each file

        yield (full_filename,
               os.stat(full_filename).st_mtime,
               os.stat(full_filename).st_ctime,
               os.stat(full_filename).st_atime)
        #filename alongwith three times
        
#Takes an iterable and a function, if function returns TRUE, then item is printed
def yield_filter(data, func):
    for one_item in data:
        if func(one_item):
            yield one_item
