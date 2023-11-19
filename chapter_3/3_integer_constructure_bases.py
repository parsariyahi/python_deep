import fractions

#help(int)

#truncate the value.
a = int(10.999999)



a = fractions.Fraction(20, 3)
print(a)
print(float(a))
print(int(a))


print(int("1234"))
print(int("111", base=2))

#bases are case insensitive.
print(int("FFFF", base=16))
print(int("ffff", base=16))


def from_base10(n, b):
    if b < 2:
        raise ValueError("b must be >= 2")
    if n < 0:
        raise ValueError("n must be positive")
    if n == 0:
        return [0]

    digits = []
    while n > 0:
        n, m = divmod(n, b)
        digits.insert(0, m)

    return digits

def encode(digits, digit_map):
    if max(digits) >= len(digit_map):
        raise ValueError("digit_map is not enough for encoding digits")

    return ''.join([digit_map[d] for d in digits])

print(from_base10(10, 2))

print(from_base10(255, 16))

print(encode(
    [15, 15], "0123456789ABCDEF"
))


def rebase_from10(number, base):
    digit_map = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if base < 2 or base > 36:
        raise ValueError("base must be 2 <= base <= 36")

    sign = -1 if number < 0 else 1
    number *= sign

    digits = from_base10(number, base)
    encoding = encode(digits, digit_map)
    if sign == -1:
        encoding = '-' + encoding

    return encoding

a = rebase_from10(3451, 16)
print(a)
print(int(a, base=16))

#Negative
a = rebase_from10(-64, 2)
print(a)
print(int(a, base=2))