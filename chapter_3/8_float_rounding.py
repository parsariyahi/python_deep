a = round(1.6)
print(a, type(a))


a = round(1.6, 0)
print(a, type(a))


a = round(1.6666, 1)
print(a, type(a))


a = round(1.6666, 2)
print(a, type(a))


a = round(1.6666, 3)
print(a, type(a))


a = round(446.22, 1)
print(a, type(a))


a = round(446.22, 0)
print(a, type(a))

## -1 is 10 ^ -(-1)
a = round(446.22, -1)
print(a, type(a))


a = round(446.22, -2)
print(a, type(a))


a = round(446.22, -3)
print(a, type(a))


## Ties 

## Banker rounding

a = round(1.25, 1)
print(a, type(a))


a = round(1.35, 1)
print(a, type(a))


## Round up
def round_up(number):
    from math import copysign
    return int(number + 0.5 * copysign(1, number))


a = round_up(1.5)
print(a)


a = round_up(2.5)
b = round(2.5)
print("Round up: ", a, " VS ", "Banker rounding: ", b)