#printing tuple records

'''
Tuples are commonly used as records like struct in C++
'''
import operator
PEOPLE = [('Donald','Trump',7.85),
          ('Vladimir','Putin',9.727),
          ('Jinping','Xi',10.609)]

def format_sort_records(list_of_tuples):
    #takes a PEOPLE list and returns a formatted string
    #Last name, first name, time
    #10 character field for name
    #5 char field for time
    output = []
    template = '{1:10} {0:10} {2:5.2f}'
    for person in sorted(list_of_tuples, key=operator.itemgetter(1,0)):
        #sorts by last name and then first name
        output.append(template.format(*person))
        #used str.format() to format the string
        #and *person becomes elements of a tuple not the tuple itself, can be accessed via {0}{1}{2}

    return output

print(format_sort_records(PEOPLE))


#Example: using namedtuple
from collections import namedtuple
Person = namedtuple('Person',['first','last','distance'])

PEOPLE = [Person('Donald','Trump',7.85),
          Person('Vladimir','Putin',9.727),
          Person('Jinping','Xi',10.609)]

def format_sort_records_1(list_of_tuples):
    output = []
    template = '{last:10} {first:10} {distance:5.2f}'
    for person in sorted(list_of_tuples, key=operator.attrgetter('last', 'first')):
        output.append(template.format(*(person._asdict())))
    return output

print(format_sort_records_1(PEOPLE))

'''
About namedtuple
'''

#example sort by field
#learn how this is similar to namedtuple

MOVIES = [('Parasite', 132, 'Bong Joon-ho'),
          ('Ford v Ferrari', 152, 'James Mangold'),
          ('The Irishman', 209, 'Martin Scorsese'),
          ('Jojo Rabbit', 108, 'Taika Waititi'),
          ('Joker', 122, 'Todd Phillips'),
          ('Little Women', 135, 'Greta Gerwig'),
          ('Marriage Story', 137, 'Noah Baumbach'),
          ('1917', 119, 'Sam Mendes'),
          ('Once Upon a Time in Hollywood', 161, 'Quentin Tarantino')
          ]

FIELDS = {'name': 0,
          'length': 1,
          'director': 2}


def sort_movies():
    sort_by = input("Enter sort field (name/length/director): ").strip()

    if sort_by in FIELDS:

        output = []
        template = '{0:30} {1:3} {2:20}'
        for one_movie in sorted(MOVIES, key=operator.itemgetter(FIELDS[sort_by])):
            output.append(template.format(*one_movie))
        return output

    print(f'No such field {sort_by}')