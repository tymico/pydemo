# Filename: file.py

import os
import glob
import time

pathname = r'e:/my_pro/python/study/file.py'
print(pathname)

(dirname, filename) = os.path.split(pathname)
print(dirname)
print(filename)

(shortname, extensiion) = os.path.splitext(filename)
print(shortname)
print(extensiion)

print(os.path.join(dirname, filename))

print(glob.glob('*.py'))

metadata = os.stat(filename)
print(metadata.st_mtime)
print(time.localtime(metadata.st_mtime))

print(os.path.realpath(filename))

print([f for f in glob.glob('*.py') if os.stat(f).st_size > 400])

