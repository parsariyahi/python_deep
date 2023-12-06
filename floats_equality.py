from math import isclose

#Approximate reperesntation in binary
a = 0.1
print(format(a, ".25f"))
a = 0.1 + 0.1 + 0.1
b = 0.3
print(a == b)

#Finite reperesntation in binary
a = 0.125
print(format(a, ".25f"))
a = 0.125 + 0.125 + 0.125
b = 0.375
print(a == b)

a = 0.1
print(format(a, ".25f"))
a = 0.1 + 0.1 + 0.1
b = 0.3
print(a == b)
print(round(a, 3) == round(b, 3))

#Round function problem
a = 0.01
b = 0.02
print(a == b)
print(round(a, 1) == round(b, 1))
print(b / a)

a = 1000.01
b = 1000.02
print(a == b)
print(round(a, 1) == round(b, 1))
print(b / a)

#Isclose function in math module
a = 0.1 + 0.1 + 0.1
b = 0.3
print(a == b)
print(isclose(a, b))

a = 123456789.01
b = 123456789.02
print(a == b)
print(isclose(a, b, rel_tol=0.01))

a = 0.01
b = 0.02
print(a == b)
print(isclose(a, b, rel_tol=0.01))

a = 0.0000001
b = 0.0000002
print(a == b)
print(isclose(a, b, rel_tol=0.01))

a = 0.0000001
b = 0.0000002
print(a == b)
print(isclose(a, b, rel_tol=0.01, abs_tol=0.01))