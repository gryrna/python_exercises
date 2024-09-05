'''
Dealing with complex data structures using LIST comprehensions

'''
def flatten(mylist):
    '''
    Takes a list of lists and returns a flat 1-D version of the list
    '''
    return [one_element
            #expression: what do we want? one element at a time
            for one_sublist in mylist
            #1st level of iteration
            for one_element in one_sublist]
            #2nd level of iteration, nested for loop
#sample
list_of_lists = [[1,2,4,5],
                 [4,6,7,3],
                 [5,7,8,2],
                 [4,8,9,1]]
print(flatten(list_of_lists))


def flatten_odd_ints(mylist):
    '''
    Same as above but filters out even elements and characters
    '''
    return [int(str(one_element))
            #expression: we want integer values at end
            for one_sublist in mylist
            #1st level of iteration
            for one_element in one_sublist
            #2nd level of iteration
            if str(one_element).strip().isdigit() and int(one_element) % 2 == 1]
            #condition for filtering, must be a digit and odd

#sample
print(flatten_odd_ints(list_of_lists))


def grandchildren_names(d):
    '''
    Takes a dict that represents children and grandchildren
    Key is child's name, while value is list of string with grandchildren name
    and returns a list of grandchildren names
    '''
    return [one_grandchild
            #expression: we want grandchildren name
            for grandchildren_list in d.values()
            #1st level of iteration using dict.values() to extract grandchildren names
            for one_grandchild in grandchildren_list]
            #2nd level of iteration for each value

#sample
d = {'Alpha': ['Bravo','Charlie','Delta'],'Echo':['Foxtrot','Golf']}
#Alpha and Echo are siblings, the rest are their children

print(grandchildren_names(d))

import operator

def sorted_grandchildren(d):
    '''
    Same as above but sorted by age
    Takes a dict of dicts where each sub-dict has 2 name-value pairs (name, age)
    for each grandchildren
    The values for 1st level key are list of dicts
    '''
    grandchildren = grandchildren_names(d)
    #using above function to create list of grandchildren

    return [[one_grandchild['name'],one_grandchild['age']]
            for one_grandchild in sorted(grandchildren,
                                         key=operator.itemgetter('age'))]
            #using sorted on grandchildren list, with sort key being age of grandchildren

d_1={'Alpha':[{'name':'Bravo','age':4},
            {'name':'Charlie','age':5},
            {'name':'Delta','age':2}],

     'Echo':[{'name':'Foxtrot','age':6},
            {'name':'Golf','age':3}]
     }


print(sorted_grandchildren(d_1))