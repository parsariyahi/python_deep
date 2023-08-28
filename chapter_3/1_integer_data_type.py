import time
import sys



print(sys.getsizeof(10))
print(sys.getsizeof(1000))
print(sys.getsizeof(1000000))
print(sys.getsizeof(10000000000))
print(sys.getsizeof(2**10000000))




def calc(number):
    for _ in range(0, 10000000):
        number * 2


start = time.perf_counter()
calc(10000)
end = time.perf_counter()
print(end-start)


start = time.perf_counter()
calc(2**10000)
end = time.perf_counter()
print(end-start)


start = time.perf_counter()
calc(2**100000)
end = time.perf_counter()
print(end-start)