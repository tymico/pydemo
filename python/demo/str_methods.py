# Filename: str_methods.py

name = 'Swaroop' # This is a string object 

if name.startswith('Swa'):
    print('Yes, the string starts with "Swa"')

if 'a' in name:
    print('Yes, it contains the string "a"')

if name.find('war') != -1:
    print('Yes, it contains the string "war"')

print(len(name))

delimiter = '_*_'
mylist = ['Brazil', 'Russia', 'India', 'China']
print(delimiter.join(mylist))

username = 'mark'
password = 'PapayaWhip'
print("{0}'s password is {1}".format(username, password))
