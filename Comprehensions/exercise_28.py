'''
Remember: DO more with LESS code while keeping it reliable and
easy to debug.
One way to achieve that is FUNCTIONAL programming.
Keep Functions short using immutable data.

Python offers comprehensions, that originiated from LISP.
Comprehensions make it easy to create LIST, SETS and DICTS based
on other Data structures.

So, even if a problem can be solved non-functional way, try to make it
using functional programming to keep it short.

When you must use COMPREHENSION?
-Whenever you want to transform an iterable(list, set, dict) into a LIST.
    e.g. convert a list of int to list of float

Use FOR loop: when you want to do something to each element of iterable.
    e.g. convert int to float and use it while not intersted in a return value

Examples:
1. Want to know age of each employee, assuming an age method exists for employee object
    [employee_age(one_employee)
    for one_employee in all_employees]
2. Know max temp of each day of previous month
    [max_temp(one_day)
    for one_day in previous_month]
3. Number of vowels in a passage, assuming count_vowels() exists for one_word
    sum((count_vowels(one_word)
        for one_word in passage))

Always break your comprehension into parts of Expression, Iteration and Condition.
This keeps the code more readable, and easy to debug.
Example:
    [(x,y)              <-Expression
    for x in range(5)   <-Iteration
    if x%2              <-Condition
    for y in range(5)   <-Another Iteration
    if y%3]             <-Another Condition

Got a list of lists? or, list of tuples?
    Use a nested LIST comprehension

'''


def join_numbers(numbers):
    '''
    Takes a series of numbers and joins them into a string with comma as separator
    '''

    return ','.join(str(item)
                    for item in numbers)
    #used generator instead of LIST comprehension to convert integer to str and make a list
    #NOTE: str.join() doesnt work on list of integers, that's why converting them to string

#sample
print(join_numbers(range(20)))



def join_under_10(numbers):
    '''
    Same as above, but only joins whole numbers that are less than 10
    '''
    return ','.join(str(item)
                    for item in numbers
                    if 0<= item <=10)
    #added an extra validation for LIST comprehension using generators

#sample
print(join_under_10(range(20)))


def sum_hexes(hex_numbers):
    '''
    Takes sequence of hex_numbers and returns their sum in decimal
    '''
    return sum(int(one_number, 16)
               for one_number in hex_numbers)
    '''
    Problem with LIST comprehension is, it creates a LIST,
    for large values, that means a lot of memory.
    So, we use Generators, that look like LIST comprehension
    but uses only () instead of []
    Generator returns one value at a time and waits for the sum()
    function to request next item
    '''

#sample
print(sum_hexes(['C8','190']))

def reverse_words(filename):
    '''
    Takes a file and reverses each line to produce it as output
    '''

    return [','.join(reversed(one_line.split()))
            for one_line in open(filename)]
    #self explanatory

