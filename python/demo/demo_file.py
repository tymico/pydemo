# Filename: using_file.py

poem = '''\
There is a pleasure in the pathless woods, 
There is a rapture on the lonely shore, 
There is a society where none intrudes, 
By the deep sea, and music in its roar; 
I love not Man the less, but Nature more, 
From these our interviews, in which I steal 
From all I may be, or have been before, 
To mingle with the Universe, and feel 
What I can never express, yet can not all conceal. 
'''

f = open('poem.txt', 'w') # open for 'w'riting
f.write(poem) # write text to file
f.close() # close the file

f = open('poem.txt')
# if no mode is specified, 'r'ead mode is assumed by default

while True:
    line = f.readline()
    if len(line) == 0: # Zero length indicates EOF
        break
    print(line, end="")
    # Notice comma to avoid automatic newline added by Python

f.close() # close the file
