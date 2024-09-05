'''
Using DICT to accumulate data over time'''

#rainfall
#a function get_rainfall to display rainfall
#  of a city over a period of time
#the function should also take input and add it to dict

#1. take input from user
#2. Check if that city key is already in dict
# if not, then create one
#3. take input for value and add it to the city
#4. for multiple enteries to same key, add them all

def get_rainfall():

    rainfall = {}

    while True:
        city_name = input('Enter city name:').strip().lower()

        if not city_name:
            break
        
        try:
            mm_rain = input('Enter mm rain: ')
            rainfall[city_name] = rainfall.get(city_name, 0) + int(mm_rain)
            #add to current rainfall, the default/start is 0, if not value is provided
            #we converted the string input to int later
            #dict.get method also checks for key already present or not
            #if no city name exists in rainfall, then we get 0 back
        except ValueError:
            continue
        
    
    for city, rain in rainfall.items():
        print(f'{city}: {rain}')

#get_rainfall()

'''more about get() method of dict
more about defaultdict from collections'''
'''A check for integer can be done using str.isdigit() method'''

#get_rainfall function that outputs total rainfall and average rainfall

def get_rainfall_1():
    rainfall = {}
    while True:
        city_name = input('Enter city name: ').strip().lower()

        if not city_name:
            break

        mm_rain = input('Enter mm rainfall: ')

        if city_name not in rainfall:
            rainfall[city_name] = []

        rainfall[city_name].append(int(mm_rain))
    
    for city, rain in rainfall.items():
        print(f'rainfall in {city}: Total {sum(rain)}, Average {sum(rain)/len(rain)}')


get_rainfall_1()