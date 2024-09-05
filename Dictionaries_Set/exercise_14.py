'''
About Dictionaries
Most important Data Structure
aka hashes, hash table, hash maps, mappings in other languages

Dict has pair of data, first part being the key
and second being the value

Key can be either int or string but must be hashable
Key is passed through a hash function and that value is used
to store the value.
Keys are immutable

Got a pair of values? Use dictionaries
e.g. records, user-password, name-dob

To retrieve value from dict, use dict[key]
dict.items() returns all key-value pairs


'''
'''
About Sets
Closely related to dicts
Sets have only keys you can say
They don't have duplicates

Both sets and dict are defined using {}
'''

'''
More About hash function
'''

#Restaurant
#create a MENU dict, keys of string type
#value be integers
#a Function restaurant asks user to input choice
#for valid choice, output the price and add it to total
#for invalid choice, output a note

MENU = {'sandwich': 10, 'tea': 7, 'salad': 9}

def restaurant():
    total = 0
    while True:
        order = input('Order: ').strip().lower()
        #we use strip() in case the user enters a bunch of spaces and not a choice
        #strip() removes leading and trailing whitespaces
        #also lock the lower case to match cases like Sandwuich, SandWich etc

        if not order:
            break
        #for empty strings, break the while loop
        #this method checks for emptiness, rather than using if (len) or if order ==''

        if order in MENU:
            price = MENU[order]
            total += price
            print(f'{order} costs {price}, total is {total}')
        #here we check for item in our dict and pull out value corresponding to
        #given key using DICT[key] method
        
        else:
            print(f'we are out of fresh {order} today')
    print(f'Your total is {total}')

#restaurant()


#using time module to display temp from known dates

from datetime import datetime, timedelta

TEMP = {'2020-08-06':30,
        '2020-08-07':32,
        '2020-08-08':32}

def temp():
    while True:
        today = input('Enter the date in YYYY-MM-DD format:').strip()
        
        #series of checks to validate input data
        if not today:
            break

        if len(today)!=10:
            print('Invalid format; try again')
            continue
        if today.count('-')!=2:
            print('Invalid format; try again')
            continue
        if today not in TEMP:
            print(f'temp for {today} is not known; try again')
            continue
        
        #final try with all valid data
        try:
            today_date = datetime.fromisoformat(today).date()
            #date conversion
        except ValueError as e:
            print(f'Not a valid date string; try again')
            continue

        #getting previous and next dates
        yesterday_date = str(today_date - timedelta(1))
        tomorrow_date = str(today_date + timedelta(1))

        #the final output
        print(f'{yesterday_date}: {TEMP.get(yesterday_date, "No data available")}')
        print(f'{today_date}: {TEMP[str(today_date)]}')
        print(f'{tomorrow_date}: {TEMP.get(tomorrow_date, "No data available")}')

#temp()

'''
About datetime module'''
