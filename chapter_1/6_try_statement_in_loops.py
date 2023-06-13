a = 10
b = 0

try:
    c = a/b
except ZeroDivisionError:
    print("zero division")
finally:
    print("just always execute")




a = 4
b = 0

while b < 3:
    b += 1
    a -= 1

    print("__________________")

    try:
        c = a/b
    except ZeroDivisionError:
        print("zero division")
        continue
    finally:
        print("just always execute")

    print("normal loop")


a = 4
b = 0

while b < 3:
    b += 1
    a -= 1

    print("__________________")

    try:
        c = a/b
    except ZeroDivisionError:
        print("zero division")
        break
    finally:
        print("just always execute")

    print("normal loop")