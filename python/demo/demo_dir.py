# Filename: using_dir.py

import sys

print('Get list of attributes for sys module:')
print(dir(sys))

print('\nGet list of attributes for current module:')
print(dir())

a = 5
print(dir())

del a
print(dir())
