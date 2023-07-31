a = 19
b = 19
c = b

print(a is b)
print(a is c)
print(b is c)


a = 4972808000
b = 4972808000
print(a is b)
print(a == b)


a = "hello"
b = "hello"
print(a is b)
print(a == b)

a = "some longer string to check some longer string to check some longer string to check "
b = "some longer string to check some longer string to check some longer string to check "
print(a is b)
print(a == b)

a = [1, 2, 3]
b = [1, 2, 3]
print(a is b)
print(a == b)


print(id(None))


a = None
b = None
c = None

print(a is b)
print(a is c)
print(c is None)