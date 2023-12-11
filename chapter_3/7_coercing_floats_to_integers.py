import math

print(math.trunc(10.9))
print(math.trunc(1.9))
print(math.trunc(1.999999))
print(math.trunc(1.0000001))
print(math.trunc(-1.0000001))


#int constructor uses truncation
print(int(10.9))
print(int(10.900009))
print(int(110.00009))


print(math.floor(20.9))
print(math.floor(21.9))
print(math.floor(-21.9))
print(math.floor(-1.000001))


print(math.ceil(20.9))
print(math.ceil(21.9))
print(math.ceil(-21.9))
print(math.ceil(-1.000001))