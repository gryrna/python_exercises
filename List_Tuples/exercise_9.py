'''
About List and Tuples
List - mutable, use for sequence of items of same type
Tuple - immutable, use for sequence of items of different types

List can be a sequence of tuples
Example: Store name and Dob in a tuple, and store all these in a list

Like other sequences, For loop can be used, 'in' operator can be applied
indexing can be used

Lists are not arrays as they don't have fixed length and type.
'''

#a function that takes a sequence
#returns first and last element of it

def first_last(sequence):
    
    # return sequence[0] + sequence[-1] #not a real solution
    return sequence[:1] + sequence[-1:]

print(first_last([1,2,3,4]))
print(first_last('abcdef'))

'''
Slice returns same data type
Indexing returns the element'''

def largest(sequence):
    if not sequence:
        return None
    output = sequence[0]
    for item in sequence[1:]:
        if item > output:
            output = item
    return output

print(largest([1,3,6,2,7,4]))
print(largest([(1,2),(3,4),(3,3)]))

def even_odd_sums(sequence):
    #adds items at even and odd indexes and presents them
    #as a two element list
    evens = []
    odds = []
    for index in range(len(sequence)):
        if index % 2: #checks for remainder
            odds.append(sequence[index])
        else:
            evens.append(sequence[index])
    return [sum(evens), sum(odds)]

print(even_odd_sums([10,20,30,40,50,60]))

def plus_minus(sequence):
    #alternative plus_minus on sequence
    #take first element, add next, subtract third and so on..
    output = sequence[0]
    for index in range(1, len(sequence)):
        if index % 2: #checks for remainder
            output += sequence[index]
        else:
            output -= sequence[index]
    return output

print(plus_minus([10,20,30,40,50,60]))

#A smart solution using pop()
#pop() returns a new list with removed element
def plus_minus(numbers):
    if not numbers:
        return 0
    total = numbers.pop(0)
    while numbers: #while True
        total += numbers.pop(0)

        if numbers: #also if True
            total -= numbers.pop(0)
    return total


def myzip(*args):
    #takes any number of iterables and returns a list of tuples.
    #The tuple at index n will have items from index n in each iterable.
    return [tuple(a[i] for a in args)
            for i in range(len(min(args, key=len)))]

'''More about POP, ZIP, Slice
'''

