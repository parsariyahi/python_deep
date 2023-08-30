import math

print(type(10 + 10))
print(type(15 - 10))
print(type(10 * 10))
print(type(10 ** 10))
print(type(10 / 10))
print(type(10 / 2))
print(type(3 / 2))


print(math.floor(3.222222))
print(math.floor(-3.222222))
print(math.floor(-3.00000000000001))
print(math.floor(-3.0000000000000001)) #Floating point limit in python.


a = 33
b = 4
print(a / b)
print(a // b)
print(math.floor(a / b))

a = -33
b = 4
print(a / b)
print(a // b)
print(math.floor(a / b))

a = 33
b = -4
print(a / b)
print(a // b)
print(math.floor(a / b))

a = 33
b = -4
print(a / b)
print(a // b)
print(math.floor(a / b))
print(math.trunc(a / b))


a = 13
b = 4
print("{0}/{1} = {2}".format(a, b, a/b))
print("{0}//{1} = {2}".format(a, b, a//b))
print("{0}%{1} = {2}".format(a, b, a%b))
print(a == b * (a//b) + (a%b)) #This equation must be true.


a = -13
b = 4
print("{0}/{1} = {2}".format(a, b, a/b))
print("{0}//{1} = {2}".format(a, b, a//b))
print("{0}%{1} = {2}".format(a, b, a%b))
print(a == b * (a//b) + (a%b)) #This equation must be true.


a = 13
b = -4
print("{0}/{1} = {2}".format(a, b, a/b))
print("{0}//{1} = {2}".format(a, b, a//b))
print("{0}%{1} = {2}".format(a, b, a%b))
print(a == b * (a//b) + (a%b)) #This equation must be true.


a = -13
b = -4
print("{0}/{1} = {2}".format(a, b, a/b))
print("{0}//{1} = {2}".format(a, b, a//b))
print("{0}%{1} = {2}".format(a, b, a%b))
print(a == b * (a//b) + (a%b)) #This equation must be true.