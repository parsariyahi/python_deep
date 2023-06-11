# simple `if` statement
a = 10

if a < 15:
    print("a < 15")
else :
    print("a >= 15")

# nested `if` statement
b = 10

if a <= 10:
    print("a <= 10")
else :
    if a == 140:
        print("a == 140")
    else:
        print("a != 140")

c = 10

if c == 11:
    print("c == 11")
elif c == 12:
    print("c == 12")


# ternary operator
# X if (condition is True) else Y

d = 10

e = d + 10 if d == 10 else 20
