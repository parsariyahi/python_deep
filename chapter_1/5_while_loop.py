# the while loop is a loop with a condition of an expresion,
# of its True the code block will run and if its not, the code wont run.

i = 5

while i < 10:
    print(i)
    i += 1

# or
# break will end the loop, it will break the loop process.

while True:
    print(i)

    if i < 11:
        break

    i += 1

# simple project with while loop

# we want to get users name and keep getting until a valid name

min_length = 2

name = input("your name: ")

while not(name.isprintable() \
    and name.isalpha() \
    and len(name) > min_length):
    name = input("your name: ")

print(name)

# or a better way to stick into DRY principle 

while True:

    name = input("your name:")

    if name.isprintable() \
        and name.isalpha() \
        and len(name) > min_length:
        break

print(name)


# continue will skip the current loop ofter the continue keyword
i = 0

while i < 10:
    i += 1
    if i % 2 == 0:
        continue
    print(i)


# else statement for while loop.
# if the loop terminate normaly,
# the else will execute.

l = [1, 2, 3]
nidle = 4
index = 0

while index < len(l):

    if l[index] == nidle:
        break

    index += 1

else:
    l.append(nidle)

print(l)