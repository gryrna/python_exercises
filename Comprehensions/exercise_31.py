'''
LIST comprehension works on anything that is iterable
and that includes files.
'''

def plword(word):
    '''
    From exercise_5
    '''

    if word[0] in 'aeiou':
        return word + 'way'
    
    return word[1:] + word[0] + 'ay'

def plfile(filename):
    '''
    Takes a filename and returns each string translated
    to pig latin
    '''
    return ' '.join(plword(one_word)
                    #expression
                    for one_line in open(filename)
                    #1st level of iteration taking each line
                    for one_word in one_line.split())
                    #2nd level of iteration taking each word
    #LIST comprehension returns a list, so we use a str.join(list_items)
    #to convert back into lines
    #and it's a generator


def funcfile(filename, func):
    '''
    This combines the two
    Takes a filename, and a function that returns a string
    Applies that function on each word of that file
    '''
    return ' '.join(func(one_word)
                    for one_line in open(filename)
                    for one_word in one_line.split())
                #generator to avoid long lists


def dicts_to_tuples(list_of_dicts):
    '''
    Takes a list of dicts and returns a list of tuple for
    each item of that dict.
    '''
    return [one_tuple
            for one_dict in list_of_dicts
            for one_tuple in one_dict.items()]

#sample
list_of_dicts = [{'name':'Bravo','age':4},
            {'name':'Charlie','age':5},
            {'name':'Delta','age':2}]
print(dicts_to_tuples(list_of_dicts))

# print(list_of_dicts[0].items())

import collections

def most_popular_hobbies(list_of_dicts):
    '''
    Takes a list of dict, each dict has 2 key-value pairs(name, hobbies)
    name is a string while hobbies is a set of strings
    
    Returns the three most common hobbies
    '''
    
    return collections.Counter([one_hobby
                                #expression: we want to count hobbies
                                for one_person in list_of_dicts
                                #1st level of iteration
                                for one_hobby in one_person['hobbies']]).most_common(3)
                                #2nd level of iteration

people = [
    {
        "name": "Alice",
        "hobbies": {"reading", "cycling", "hiking", "music"}
    },
    {
        "name": "Bob",
        "hobbies": {"cooking", "gaming", "photography", "music"}
    },
    {
        "name": "Charlie",
        "hobbies": {"painting", "traveling", "gardening", "reading"}
    },
    {
        "name": "Diana",
        "hobbies": {"running", "knitting", "music", "cycling"}
    },
    {
        "name": "Eve",
        "hobbies": {"yoga", "swimming", "writing", "reading"}
    },
    {
        "name": "Frank",
        "hobbies": {"hiking", "fishing", "cycling"}
    },
    {
        "name": "Grace",
        "hobbies": {"photography", "traveling", "cooking"}
    },
    {
        "name": "Hannah",
        "hobbies": {"writing", "yoga", "painting", "running"}
    },
    {
        "name": "Isaac",
        "hobbies": {"gaming", "photography", "swimming"}
    },
    {
        "name": "Jasmine",
        "hobbies": {"gardening", "music", "knitting", "traveling"}
    }
]

print(most_popular_hobbies(people))