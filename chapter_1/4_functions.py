# Some are built-in functions 
l = [1, 2, 4]

lenght = len(l)

# Some are inside packages
from math import sqrt

print(sqrt(4))

# or we can import all

import math

print(math.pi)

# We can define our functions 

def func_1():
    print("inside func_1")

print(func_1) # this is the function object itself
func_1() # this will call or invoke the function


# We can have parameters for our functions

def func_2(a, b):
    return a + b

# And we can annotate the types for our parameters

def func_2(a: int, b: int) -> int:
    return a + b


def func_3():
    return func_4()

def func_4():
    print("inside func 4")


# We have lambda functions that just create functions in diffrent  syntax

fn = lambda x: x - 1

print(fn(10))