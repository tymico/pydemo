# Filename: using_other.py

exec('print("Hello World")')

print(eval('2 * 3'))

mylist = ['item']

# repr函数用来取得对象的规范字符串表示。注意，在大多数时候有eval(repr(object)) == object。
print(repr(mylist))


assert len(mylist) > 1
