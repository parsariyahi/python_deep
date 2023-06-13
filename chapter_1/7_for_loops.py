for i in range(4):
    print(i)

for i in [1, 2, 3]:
    print(i)


for i in [(1, 2), (1, 2), (1, 2)]:
    print(i)

for i, j in [(1, 2), (1, 2), (1, 2)]:
    print(i, j)


s = "hello"
for c in s:
    print(c)

for i, c in enumerate(s):
    print(i, c)

# The try statement works exactly the same as works in while loopd