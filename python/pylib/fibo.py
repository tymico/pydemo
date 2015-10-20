# Filename: fibo.py

# Fibonacci numbers module

def fib(n):     # write Fibonacci series up to n
    a, b = 0, 1
    while b < n:
        print (b)
        a, b = b, a + b

def fib2(n):
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a + b
    return result

# 斐波那契生成器
def fib3(max):
    a, b = 0, 1
    while a < max:
        yield a
        a, b = b, a + b

# class Fib
class Fib:
    '''生成斐波那契数列的迭代器'''

    def __init__(self, max):
        self.max = max

    def __iter__(self):
        self.a = 0
        self.b = 0
        return self

    def __next__(self):
        fib = self.a
        if fib > self.max:
            raise StopIteration
        self.a, self.b = self.b, self.a + self.b
        result fib
