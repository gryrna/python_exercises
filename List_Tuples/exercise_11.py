#capitalize alphabetic names and sort them with last names
'''
For python, Variables defined outside the function are considered
CONSTANTS and always capitalized
'''
import operator

PEOPLE = [{'first':'gary', 'last':'rana','email':'xyz@email.com'},
          {'first':'gumesh', 'last':'singh','email':'abc@email.com'},
          {'first':'don', 'last':'raja','email':'pqr@email.com'}
          ]

def alphabetize_names(list_of_dicts):
    return sorted(list_of_dicts, key=operator.itemgetter('last','first'))


print(alphabetize_names(PEOPLE))

#sort the strings based on number of vowels in words
#first count the vowels
#use that function to sort the string

def vowel_count(one_word):
    count = 0
    for one_character in one_word:
        if one_character in 'aeiou':
            total += 1
    return total

def sort_by_vowel(words):
    return sorted(words, key=vowel_count)



'''About Operator

itemgetter example
s = 'abcdef'
t = (10,20,40,50,90)
get_2_and_4 = operator.itemgetter(2,4)
print(get_2_and_4(s)) -> prints c and e as tuple
print(get_2_and_4(t)) -> prints 40 and 90 as tuple
'''
