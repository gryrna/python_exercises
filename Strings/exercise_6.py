#pig latin sentence

def pl_sentence(sentence):
    words = sentence.split()
    for word in words:
        if word[0].lower() in 'aeiou':
            print(f'{word}way', end=" ")
        else:
            print(f'{word[1:]}{word[0]}ay', end=" ")

pl_sentence('this is a test')

def transpose_strings(list_of_words):
    '''given a list of strings, each of which contains multiple words
    transpose them. so given input of
    ['abc def ghi', 'jkl mno pqr', 'stu vwx yz']
    the output should be
    ['abc jkl stu', 'def mno vwx' 'ghi pqr yz']'''

    return [' '.join(t)
            for t in (zip(*[s.split()
                           for s in list_of_words]))]

print(transpose_strings(['abc def ghi', 'jkl mno pqr', 'stu vwx yz']))

'''About Split()
'''

