#how many different numbers

#a function that returns the number of different integers it contains

def numbers_count(list_of_numbers):
    return set(list_of_numbers)

numbers = [1,2,3,1,2,3,4,1]

print(numbers_count(numbers))

#whenever we want unique, use set

'''
Use set.add() to add more enteries to it
set.update() to add more than one item at a time'''


