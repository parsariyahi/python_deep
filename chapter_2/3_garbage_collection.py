import ctypes
import gc

def ref_count(memory_address):
    return ctypes.c_long.from_address(memory_address).value

def obj_by_id(memory_address):
    for obj in gc.get_objects():
        if id(obj) == memory_address:
            return "OBJ Found"

    return "OBJ Not Found"

gc.disable()


class A:

    def __init__(self):
        self.b = B(self)

class B:

    def __init__(self, a):
        self.a = a

var = A()

a_id = id(var)
b_id = id(var.b)

print(ref_count(id(var)))
print(ref_count(id(var.b)))
print(ref_count(id(var.b.a))) # A itself

var = None

print(ref_count(id(a_id)))
print(ref_count(id(b_id)))

print(obj_by_id(a_id))
print(obj_by_id(b_id))

gc.collect()

print(obj_by_id(a_id))
print(obj_by_id(b_id))

# here we will get wierd numbers because the momory is reclaim,
# or no longer blongs to python, the garbage collector, collected the objects.
print(ref_count(id(a_id)))
print(ref_count(id(b_id)))