a = 10
print(hex(id(a)))

a = 20
print(hex(id(a)))

a = a + 10
print(hex(id(a)))

#They are pointing the same objects
#Int's are immutable
a = 30
b = 30
print(hex(id(a)))
print(hex(id(b)))