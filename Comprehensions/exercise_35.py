'''
DICT and Comprehension are more powerful
because you can do a lot with your data in DICT form
'''
import string

def alpha_num():
    '''
    Creates a DICT object whose keys are English alphabets
    and values are numbers from 1 to 26
    '''
    return {char: index
            #expression: we want a DICT
            for index, char in enumerate(string.ascii_lowercase, 1)}
            #enumerate, numbers the items one at a time, starting from 1 instead of 0
            #the output is unpacked into index, char

#sample
print(alpha_num())

def read_config(filename):
    '''
    Take a config file where userID and Value are separated by =
    either read all
    or read only digit values using int
    '''
    return {one_line.split('=')[0]: int(one_line.split('=')[1].strip())
            #expression: we want a DICT
            #split the line at '=' and use items of that split
            #got to use int, else values will be string
            for one_line in open(filename)
            #iteration
            if one_line.split('=')[1].strip().isdigit()
            }
            #condition, the value must be a digit

#sample
file = 'Python_Workout/Comprehensions/name,value.txt'
print(read_config(file))


import json
def city_population(filename):
    '''
    Takes a JSON format file
    Creates a DICT with city as key and value as population
    Remember JSON as LIST of Dicts
    '''
    return {one_city['city']: one_city['population']
            #expression
            for one_city in json.load(open(filename))
            #iteration over each item using JSON.LOAD()
            }

def city_state_population(filename):
    '''
    Same as above but includes STATE
    '''
    return {(one_city['city'], one_city['state']): one_city['population']
            for one_city in json.load(open(filename))
            }

#sample
cities = 'Python_Workout/Comprehensions/cities.json'
# for city,population in city_population(cities).items():
#     print(f'{city}: {population}')
for city,population in city_state_population(cities).items():
    #unpacking dict gives key and value, here key is a tuple
    print(f'{city}: {population}')


GEMATRIA = alpha_num()
#creating a DICT object from function


def gematria_for(word):
    '''
    Take a single word(string) and returns
    the Gematria score for that word'''
    return sum(GEMATRIA.get(one_char, 0)
               #get value of DICT item using DICT.GET(key, default value)
               for one_char in word.lower()
               #iteration for each character
               )
#sample
print(gematria_for('HUMAN'))

def gematria_equal_words(input_word):
    '''
    Takes a single word and return a list of those
    dict words whose gematria scores match the current
    word score
    Example: Gematria score for HUMAN is 8+21+13+1+14=57
    '''
    our_score = gematria_for(input_word.lower())
    #initializing using above function to have sum value
    return [one_word.strip()
            for one_word in open('/share/dict')
            #iterating over file name
            if gematria_for(one_word.lower()) == our_score
            #condition, if that word's score match our score
            ]


def dict_f_to_c(dict_of_temps):
    '''
    Takes a DICT and returns a new DICT with values converted
    '''
    return {key: (value-32)/1.8
            for key, value in dict_of_temps.items()}

#sample
india_city_temperatures = {
    "New Delhi": 95,
    "Mumbai": 88,
    "Bengaluru": 77,
    "Chennai": 85,
    "Kolkata": 90,
    "Hyderabad": 82,
    "Pune": 78,
    "Ahmedabad": 92,
    "Jaipur": 97,
    "Chandigarh": 93
}
print(dict_f_to_c(india_city_temperatures))


def make_people_data(people):
    return {city: {'first': name.split()[0],
                    'last':name.split()[1],
                    'per capita': per_capita}
                    for name, city, per_capita in people}
#sample
people_data = [
    ("Amit Sharma", "New Delhi", 2500),
    ("Priya Patel", "Mumbai", 3200),
    ("Raj Singh", "Bengaluru", 2700),
    ("Anita Rao", "Chennai", 2800),
    ("Ravi Kumar", "New Delhi", 2600),
    ("Sneha Desai", "Hyderabad", 2900),
    ("Arjun Mehta", "Pune", 2750),
    ("Neha Gupta", "Ahmedabad", 3000),
    ("Vikram Verma", "Jaipur", 3100),
    ("Aisha Khan", "Chandigarh", 2950)
]
print(make_people_data(people_data))  
