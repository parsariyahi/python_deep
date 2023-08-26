import sys

a = "hello_world"
b = "hello_world"

print( a == b)
print( a is b)

a = "hello world"
b = "hello world"

print( a == b)
print( a is b)


a = sys.intern("hello there im parsa, learning python in depth.")
b = sys.intern("hello there im parsa, learning python in depth.")
c = "hello there im parsa, learning python in depth."

print(a is b)
print(a is c)


a = "hello world, here is a long long looooong string." * 1000000
b = "hello world, here is a long long looooong string." * 1000000
print( a == b)
print( a is b)


a = "hello_world_here_is_a_long_long_looooong_string" * 1000000
b = "hello_world_here_is_a_long_long_looooong_string" * 1000000
print( a == b)
print( a is b)


a = sys.intern("hello world, here is a long long looooong string." * 1000000)
b = sys.intern("hello world, here is a long long looooong string." * 1000000)
print( a == b)
print( a is b)