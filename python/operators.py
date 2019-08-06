#!/usr/bin/python3
# ##Opeartors
# ### Arithmetic Opeartors
# Arithmetic operators are used to perform mathematical operations like
# addition, subtraction, multiplication etc.

# - //	Floor division - division that results into whole number adjusted to
#   the left in the number line	x // y
# - **	Exponent - left operand raised to the power of right
#   x**y (x to the power y)
# start
z = 2**5
y = 14//5
print('14 // 5 is {0}'.format(y))
print('2 power 5 is {0}'.format(z))
print('2 power 5 is ', z)
# end
# ###Logical operators
# - and	True if both the operands are true	x and y
# - or	True if either of the operands is true	x or y
# - not	True if operand is false (complements the operand)	not x
# - for non boolain values 0 and empty string '' will be considered as
# false non-empty strings and non zero numbers considered as true
# - for strings and numbers if both are true and will return second or will
# return first
# start
print('Logical Opeartors with numbers')
x1 = 1
x2 = 3
x3 = 0
x4 = -1
print(x1 and x2)
print(x1 or x2)
print(x3 and x1)
print(x1 or x3)
print(x1 and x4)
print(x1 or x4)
print('Logical Opeartors with strings')
x = 'that'
y = 'this'
print(x and y)
# end
# ####Bitwise operators
# Bitwise operators act on operands as if they were string of binary digits.
# It operates bit by bit, hence the name.

# For example, 2 is 10 in binary and 7 is 111.
# - & 	Bitwise AND 	x & y = 0 (0000 0000)
# - | 	Bitwise OR 	x | y = 14 (0000 1110)
# - ~ 	Bitwise NOT 	~x = -11 (1111 0101)
# - ^ 	Bitwise XOR 	x ^ y = 14 (0000 1110)
# - >> 	Bitwise right shift 	x>> 2 = 2 (0000 0010)
# - << 	Bitwise left shift 	x<< 2 = 40 (0010 1000)

# ####Assignment operators

# Assignment operators are used in Python to assign values to variables.
# a = 5 is a simple assignment operator that assigns the value 5 on the right
# to the variable a on the left.

# There are various compound operators in Python like a += 5
# that adds to the variable and later assigns the same.
# It is equivalent to a = a + 5.

# - = 	x = 5 	x = 5
# - += 	x += 5 	x = x + 5
# - -= 	x -= 5 	x = x - 5
# - *= 	x *= 5 	x = x * 5
# - /= 	x /= 5 	x = x / 5
# - %= 	x %= 5 	x = x % 5
# - //= 	x //= 5 	x = x // 5
# - **= 	x **= 5 	x = x ** 5
# - &= 	x &= 5 	x = x & 5
# - |= 	x |= 5 	x = x | 5
# - ^= 	x ^= 5 	x = x ^ 5
# - >>= 	x >>= 5 	x = x >> 5
# - <<= 	x <<= 5 	x = x << 5

# #### Special operators
# Python language offers some special type of operators like the
# identity operator or the membership operator.
# is True if the operands are identical (refer to the same object) 	x is True
# is not True if the operands are not identical
# (do not refer to the same object) x is not True
# - is will compare both operands ids and returns boolian result
# - is will compare both operands ids and returns inverted boolian result
# start
print('IDENTITY OPERATORS')
x = 3
y = 3
print(id(x), id(y))
print(x is y)
x = x+2
print(x)
print(id(x), id(y))
print(x is y)
print(x is not y)
# end
# ####Membership operators
# - *in* and *not in* are the membership operators in Python.
# - They are used to test whether a value or variable is found in a sequence
# - (string, list, tuple, set and dictionary).
# - In a dictionary we can only test for presence of key, not the value.
# - in 	True if value/variable is found in the sequence 	5 in x
# - not in 	True if value/variable is not found in the sequence 5 not in x
# start
print('MEMBERSHIP OPERATORS')
s = 'string1'
print('s' in s)
print('s' not in s)
print('d' in s)
print('d' not in s)
# end
# #### Ternary operators
# -syntax `x = a if condition else b` if condition is true a will be returned
# if condition is fase b will be returned
# start
print('Ternary operators')
a = 30
b = 80
c = 40
x = a if c > 30 else b
print(x)
