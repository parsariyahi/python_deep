a = 10
print(type(a))

# help(int)

c = int() #The default is 'ZERO' (0)
c = int("10010", base=2)
print(c)


def func(a):
    return a + 10

print(type(func))

func_2 = func

print(func_2 is func)

print(func_2(10))


def exec_func(fn, arg):
    return fn(arg)

print(exec_func(func, 10))