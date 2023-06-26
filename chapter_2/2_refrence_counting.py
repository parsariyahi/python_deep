import ctypes
import sys

def get_ref(memory_address: int):
    #This will get the memory address itself.
    return ctypes.c_long.from_address(memory_address).value

a = [1, 2]
b = a

print(sys.getrefcount(a))

print(get_ref(id(b)))