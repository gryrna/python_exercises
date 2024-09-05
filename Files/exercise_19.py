#/etc/passwd to dict
#turn a file into a more complex data structure, like Dict
#use passwd.txt file for this exercise, the file has COLON(:) separated fields
#index 0 -> username, index 2 -> user ID

#function should return a dict in which the key=username, and value=user IDs

'''
String methods like str.startswith(), str.endswith() and str.strip()
are really helpful when doing analysis and manipulation with strings'''


def pass_to_dict(filename):
    users = {}
    #initiating an empty dict, we don't know keys, so just an empty one

    with open(filename) as passwd:
        #opening the file using 'with'
        for line in passwd:
            #iterating over each line of the file
            if not line.startswith(('#','\n')):
                #skipping lines that are comments or blank lines
                #the comments, if not skipped, will return an indexError when trying to update our dict
                user_info = line.split(':')
                #making a list of contents of that line separated by a colon
                users[user_info[0]] = int(user_info[2])
                #updating the empty dict with the username and user ID
    return users

filename = 'Python_Workout/Files/passwd.txt'

# print(pass_to_dict(filename))

'''
It is easier and faster to work with structured data rather than strings
so always try to convert raw data(string) into a structured type
for example, CSV to Dict'''

#example: from passwd.txt create a dict which has last field as key, and
#list of users as value

from collections import defaultdict

def shell_users(filename):
    output = defaultdict(list)

    for one_line in open(filename):
        if one_line.startswith(('#','\n')):
            continue
        username, *ignore, shell = one_line.strip().split(':')

        output[shell].append(username)
    return output

print(shell_users(filename))

#example: Create a dict with key=usernames and value=dict with key for
#  userID, home directory and shell

def user_info(filename):
    output = {}

    for one_line in open(filename):
        if one_line.startswith(('#', '\n')):
            continue
        username, passwd, uid, *ignore, homedir, shell = one_line.strip().split(':')

        output[username] = {'uid': uid,
                            'homedir': homedir,
                            'shell': shell}

    return output

