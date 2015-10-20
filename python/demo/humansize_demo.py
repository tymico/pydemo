# Filename: humansize_demo.py

import humansize
import sys

si_suffixes = humansize.SUFFIXES[1000]
print(si_suffixes)
print('1000{0[0]} = 1{0[1]}'.format(si_suffixes))
print('1024{0[0]} = 1{0[1]}'.format(humansize.SUFFIXES[1024]))

print('1MB = 1000{0.modules[humansize].SUFFIXES[1000][0]}'.format(sys))

print(humansize.approximate_size(1024, True))
print(humansize.approximate_size(1000, False))
