#summing numbers

def mysum(*numbers):
    output = 0
    for number in numbers:
        output += number
    return output

print(mysum(1,2,3,4,5,6,7,8,9))

def mysum_1(numbers, start=0):
    output = start
    for number in numbers:
        output += number
    
    return output

print(mysum_1([1,2,3,4],50))

def summarize(words):
    #accepts a list of strings
    word_lengths = [len(one_word) for one_word in words]

    return min(word_lengths), max(word_lengths), sum(word_lengths)/len(word_lengths)

print(summarize(['this', 'is', 'a', 'test', 'string']))


def is_int(input):
    try:
        int(input)
        return True
    except ValueError:
        return False

def sum_intable(items):
    #accepts a list of python objects and sums those that can be integers
    return sum(one_item
               for one_item in items
               if is_int(one_item))

print(sum_intable(['a',6,8,'c',6,'b']))

#throws an error for input ['5',11]
