a = 10
b = a

print(id(a))
print(id(b))

a = 11
b = 11

print(id(a))
print(id(b))

a = "hello"
b = "hello"

print(id(a))
print(id(b))

a = [1, 2, 3]
b = a

print(id(a))
print(id(b))

a.append(100)

print(a)
print("b: ", b)