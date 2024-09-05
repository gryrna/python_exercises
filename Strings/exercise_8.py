#sorting a string

#can't use sorted() as it returns a list
#or use it with a join()

def strsort(words):
    return ''.join(sorted(words))

print(strsort('akiemcownryq'))

'''
About Sorted


mylist = ['abcd', 'efg', 'hi', 'j']
print(sorted(mylist, key=len))
The list will be sorted with increasing order of length

numbers = [-1,1,-6,8,-4,9]
print(sorted(numbers, key=abs))

Key can be any function.
Functions are objects and can be passed as arguments to other objects.
'''