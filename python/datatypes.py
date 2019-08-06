#!/usr/bin/python
# ## python data types
# - Integer data type:
# - float
# - complex number
# - boolean True False
# - string
# - list
# - set
# - dict
# - tuple
# ## type casting in python
# - int and float
# start
a = 20
print type(a)
b = float(a)
print b
print type(b)
# end
# - decimal hex(integer) oct(integer) int(hex) int(oct)
# start
print hex(26)
print oct(26)
print int(0x1a)
# end
# - string int float
# start
s1 = str(a)
s2 = str(b)
print s1
print type(s1)
print s2
print type(s2)
s3 = '50'
c = int(s3)
d = float(s3)
print c
print d
s4 = 'a'
print ord(s4)
# end
# ord() is used to get unicode value of the given charector
# an errror will be raised when multiple chars are feeded like 'ab'
# start
s6 = 'viisshnu'
l = list(s6)
print l
print tuple(s6)
print set(s6)
# end

