from fractions import Fraction


print("float of 10: ", float(10))
print("float of 10 in string: ", float('10'))

print("float of a float : ", float(10.2))


print("float of a fraction: ", float(Fraction('22/7')))

print("display of 0.1: ", float(0.1))
print("displat of 0.1 with 15 decimal points: ", format(0.1, ".15f"))
print("displat of 0.1 with 15 decimal points: ", format(0.1, ".25f"))
#NOTE: 0.1 does not have exact representation in binary, the value is not finite

print("float of 0.125", format(0.125, ".25f"))



a = 0.1 + 0.1 + 0.1
b = 0.3

print(a == b)
print("a with 25 decimal points: ", format(a, ".25f"))
print("b with 25 decimal points: ", format(b, ".25f"))