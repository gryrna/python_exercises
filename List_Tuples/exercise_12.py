#Words with most repeated letters
#a function that outputs the strings that contains greatest number
#repeated words

#so, for each word find the letter that appears the most
#them, find the word, whose most-repeated letter appears more than any other

#first find a way to count letter in a word
#that can be done using Counter module

from collections import Counter

WORDS = ['this','is','an','elementary','test','example']

def most_repeating_letter_count(word):
    return Counter(word).most_common(1)[0][1]


def most_repeating_word(list_of_words):
    return max(list_of_words, key=most_repeating_letter_count)

print(most_repeating_word(WORDS))

'''
About Counter
Counter inherits from Dict and can do whatever Dict can
example: Counter('abcabcabbbc')
>>{'a':3, 'b': 5, 'c': 3}

The most_common() sorts the counter object with most to least common
most_common(1) <- shows only the first entry
most_common(1)[0][1] <- shows count of the first entry

Like sorted, the max() also takes function as argument to key
'''
