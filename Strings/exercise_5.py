#pig latin
#add 'way' if the word starts with a vowel
#strip first character, join it at the end, add 'ay' for all other cases

def pig_latin(word):
    if word[0].lower() in 'aeiou':
        return f'{word}way'
    else:
        return f'{word[1:]}{word[0]}ay'
    
print(pig_latin('air'))
print(pig_latin('door'))

'''About Slicing
'''

'''
About Mutable and Immutable
If the object can't be changed - immutable
Strings and Tuples are immutable
'''