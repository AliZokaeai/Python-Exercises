import ctypes


def ref_count(address):
    return ctypes.c_long.from_address(address).value


my_var = [1, 2, 3, 4]
print(ref_count(id(my_var)))


import sys
print(sys.getrefcount(my_var))


other_var = my_var

print(hex(id(my_var)), hex(id(other_var)))
print(ref_count(id(my_var)))


other_var = None

print(ref_count(id(my_var)))

