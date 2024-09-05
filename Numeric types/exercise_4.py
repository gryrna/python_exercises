#hexadecimal output

def hex_output():
    dec_num = 0
    hex_num = input('enter a hex number to convert: ')
    for power,digit in enumerate(reversed(hex_num)):
        dec_num += int(digit, 16) * (16**power)
    print(dec_num)

hex_output()

'''
About function enumerate()
enumerate(iterable, start=0)
Returns an enumerate object. Iterable must be a sequence, an iterator, or some iterable object
Example:
seasons = ['spring', 'summer', 'fall', 'winter']
list(enumerate(seasons))
>>[(0,'spring'),(1,'summer'),(2,'fall'),(3,'winter')]
For start=1
>>[(1,'spring'),(2,'summer'),(3,'fall'),(4,'winter')]

About function reversed()
reversed(sequence)
returns a reverse iterator. Sequence must be an object that supports __reversed__() method
or supports the __len__() method'''
