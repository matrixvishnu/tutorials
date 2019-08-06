#!/usr/bin/python
# ### id(object)
# Return the "identity" of an object. This is an integer which is guaranteed to
# be unique and constant for this object during its lifetime. Two objects with
# non-overlapping lifetimes may have the same id() value.
import sys
# start
s = 10
print id(s)

l = [1, 2, 3]
print id(l[0])
print id(l[1])
print id(l)

# ### type(object)
# will give the type of the object it can be used in debugging
print type(l)


class d:
    x=10
    y=20
print d()
print id(d)
a = d()
print id(a)
print id(a)

# ### sys.getsizeof(object) will return the size of obj
l = range(100)
print sys.getsizeof(l)
