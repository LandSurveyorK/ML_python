def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while b < n:
        print(b, end=' ')
        a, b = b, a+b
    print()

def fib2(n):   # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a+b
    return result



def scope_test():
    def do_local():
        spam = "local spam"
    
    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"
    
    def do_global():
        global  spam
        spam = "global spam"
    
    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:",spam)
    do_global()
    print("After global assignment:",spam)

scope_test()
print("In global scope",spam)    
    
    
####
class MyClass:
    """ A simple example class"""
    i = 12345
    
    def f(self):
        return "hello world"
    
    def __init__(self):
        self.data = []

x = MyClass()


class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart
        
x = Complex(3.0,-4.5)
x.r, x.i

x.counter = 1
while x.counter < 10 :
    x.counter = x.counter *2
print(x.counter)
del x.counter

x = MyClass()
x.f()
xf = x.f()
while True:
    print(xf())
  
    
#################################################

# Timer of program processing

import numpy as np
import time
import when_will_it_end as wwie

number_of_iterations = 10

print('Starting time: ' + wwie.format_time(time.time()))

lpm = wwie.LoopProgressMonitor(n = number_of_iterations)
for k in range(number_of_iterations):
    lpm()
    _ = np.random.uniform(0,1,size=100000000)

print('Actual ending time: ' + wwie.format_time(time.time()))

##############################################


class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)
        
    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)
    
    __update = update # private copy of original update() method
    
class MappingSubclass(Mapping):
    
    def update(self, keys, values):
        # provide ne signature for update()
        # but does not break __init__()
        
        for item in zip(keys,values):
            self.items_list.appebd(item)
            
# Odds and Ends

class Employee:
    pass

john = Employee()
john.name = "John Doe"
john.dept = 'computer lab'
john.salsry = 10000



# Iterator

for element in [1,2,3]:
    print(element)
for element in (1,2,3):
    print(element)
for key in {"one":1,"two":2}:
    print(key)
for char in "123":
    print(char)
for line in open("example.txt"):
    print(line, end="")
    


























































