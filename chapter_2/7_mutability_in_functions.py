#immutable
def modify_str(string):
    string = string + " some str"
    return string

my_str = "parsa"

print(modify_str(my_str))
print(my_str)


#mutable
def modify_list(list_):
    list_.append(1000)
    return list_

my_list = [1, 2, 3]

print(modify_list(my_list))
print(my_list)


#immutable with mutable objects inside them
def modify_tuple(tuple_):
    tuple_[0].append(100)
    return tuple_

my_tuple = ([1, 2, 3], "a", 10)

print(modify_tuple(my_tuple))
print(my_tuple)