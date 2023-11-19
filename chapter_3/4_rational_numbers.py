import math
from fractions import Fraction

print("fraction 1: ", Fraction(1))

print("fraction 1 / 2: ", Fraction(1, 2))

print("fraction 0.125: ", Fraction(0.125))

print("fraction 22/7: ", Fraction("22/7"))

a = Fraction(3, 2)
b = Fraction(4, 2)
print("a + b: ", a + b)
print("a * b: ", a * b)

print("fraction -1 / 2: ", Fraction(-1, 2))

print("fraction 1 / -2: ", Fraction(1, -2))


a = Fraction(5, 9)
print("a: ", a)
print("a numerator: ", a.numerator)
print("a denominator: ", a.denominator)


F_PI = Fraction(math.pi)
print("fraction PI: ", F_PI)
print("float PI: ", float(F_PI))


SQRT_2 = Fraction(math.sqrt(2))
print("fraction sqrt 2: ", SQRT_2)
print("float sqrt 2: ", float(SQRT_2))


print("fraction 0.125: ", Fraction(0.125))
print("fraction 0.3: ", Fraction(0.3))

print(format(0.3, "0.15f"))
print(format(0.3, "0.25f"))


a = Fraction(0.3)
print("fraction 0.3 (limit denominator): ", a.limit_denominator(10))