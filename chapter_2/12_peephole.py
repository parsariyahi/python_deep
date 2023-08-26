import string
import time

def func():
    a = 24 * 60
    b = (1, 2) * 3
    c = "parsa" * 3
    d = "long string" * 10000
    f = ["a", "b"] * 5 #Lists are mutable.


print(func.__code__.co_consts)


def func1(e):
    if e in {1, 2, 3}:
        pass

print(func1.__code__.co_consts)


def func2(e):
    if e in [1, 2, 3]:
        pass

print(func2.__code__.co_consts)


print(string.ascii_letters)

char_list = list(string.ascii_letters)
char_tuple = tuple(string.ascii_letters)
char_set = set(string.ascii_letters)

def membership_test(n, container):
    for _ in range(n):
        if "z" in container:
            pass


start = time.perf_counter()
membership_test(10000000, char_list)
end = time.perf_counter()
print("list: ", end-start)

start = time.perf_counter()
membership_test(10000000, char_tuple)
end = time.perf_counter()
print("tupe: ", end-start)

start = time.perf_counter()
membership_test(10000000, char_set)
end = time.perf_counter()
print("set: ", end-start)