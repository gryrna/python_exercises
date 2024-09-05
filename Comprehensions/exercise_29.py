'''
map(function, iterable)
    -does the same job as LIST comprehension but doesn't filter out
    -returns a transformed terable from an iterable
filter(function, iterable)
    -does the job of filtering out elements
    -doesn't trasform the iterable

LIST comprehensions does both, it maps and filter the iterable

An expression, in Python, is anything that returns a value.

'''

def sum_numbers(numbers):
    '''
    Takes a sequence of strings that are separated by spaces and turns them into integers
    and returns the sum
    '''
    return sum(int(item)
               for item in numbers.split()
               if item.isdigit())
    #a three part GENERATOR comprehension with expression, iteration and condition
    #result of comprehension is returned to sum() one at a time
    #so only passes the item if it is a digit

#sample
print(sum_numbers('10 abc 20 aert 04 fg'))

def lines_with_1v40c(filename):
    '''
    Takes a file as input and outputs only those lines that 
    have min one vowel and 40 characters
    The result is a list of lines.
    '''
    return [one_line
            #expression
            for one_line in open(filename)
            #iteration
            if len(one_line) >= 40 and
            #condition 1
            len(set('aeiou') & set(one_line)) >= 1]
            #condition 2 using set intersection

#sample
filename = 'Python_Workout/Comprehensions/passage.txt'
for item in lines_with_1v40c(filename):
    print(item)

def increment_area_code(full_phone_number):
    '''
    Takes a phone number in XXX-YYY-ZZZ format
    and updates the XXX part if YYY begins from o-5
    '''
    area_code, phone_number = full_phone_number.split('-',1)
    #splitting the string with max two splits
    if phone_number[0] in '012345':
        area_code = str(int(area_code) + 1)
    return f'{area_code} - {phone_number}'
    #the output is new number

#sample
phone_numbers = ['123-456-7890',
                 '123-333-4444',
                 '123-777-8888']
for item in phone_numbers:
    print(increment_area_code(item))



def age_in_months(list_of_people):
    '''
    Takes a list of dict where each dict has 2 key-value pairs(name, age)
    Returns a new list of dict where each dict has 3 key-value pairs(name, age, age_in_months)
    only for people younger than 20 yrs
    '''
    return [dict(**one_person, age_in_months = one_person['age'] * 12)
            #expression
            #creates a dict with original key-value(**one_person) and new key-value(age_in_months=)
            #remember dict(key1 = value1, key2 = value2)
            for one_person in list_of_people
            #iteration for each individual dict in list
            if one_person['age'] <= 20]
            #condition

#sample
people = [{'name': 'A', 'age': 20},
          {'name': 'B', 'age': 21},
          {'name': 'C', 'age': 19},
          {'name': 'D', 'age': 23},
          {'name': 'E', 'age': 24}]

print(age_in_months(people))