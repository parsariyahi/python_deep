"""
Mutable objects:
    - lists
    - dicts
    - sets
    - user-defined classes

Immutable objects:
    - numbers(int, float, bool, etc)
    - strings
    - tuples
    - frozen sets
    - user-defined classes
"""

l = [1, 2, 3]
l.append(4)
print(l)
print(hex(id(l)))


t = (1, 2, 3)
print(t)
print(hex(id(t)))


t2 = ([1,2], [3,4])
print(t2)
print(hex(id(t2)))

print(t2[0])
print(hex(id(t2[0])))

t2[0].append(10)
print(t2)
print(hex(id(t2)))

print(t2[0])
print(hex(id(t2[0])))