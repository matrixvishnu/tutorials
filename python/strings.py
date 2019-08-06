#!/usr/bin/python3
# ### Strings
# #### _builtin string functions_
# - chr() 	Converts an integer to a character
# - ord() 	Converts a character to an integer
# - len() 	Returns the length of a string
# - str() 	Returns a string representation of an object
# start
print('built in string functions')
print(chr(5))
i = chr(24)
print(str(i))
print(ord('@'))
s = 'this is a string '
print('length of the string is', len(s))
l = [1, 2, 3]
print(str(l))
print(s[16])
# end
# we will get index out of range if we pass 17
# since length is 17 and last index is 16 hence the error
# #### string slicing
# Python also allows a form of indexing syntax that extracts substrings from
# a string, known as string slicing.
# start
s = 'HYDERABAD'
print('string is ', s)
print(s[2:5])  # s[start:end] will get start position and position before end
print(s[-2])  # s[-1] = last position of the string
print('to get first n chars s[:n] let n = 3:', s[0:3])
print('to get last n chars s[n:] let n = 3:', s[3:])
print('If we pass first index grater than secoend we will get empty', s[4:1])

# end
# #### shride
# Adding an additional : and a third index designates a stride
# (also called a step), which indicates how many characters to jump after
# retrieving each character in slice

print(s[1:-1:2])

# #### F-strings (works in only python 3)
# A formatted string literal or f-string is a string literal that is prefixed
# with 'f' or 'F'. These strings may contain replacement fields,
# which are expressions delimited by curly braces {}.
# While other string literals always have a constant value,
# formatted strings are really expressions evaluated at run time.
# in the expression we can also call a method
# start
print('\nF strings')
name = 'vishnu'
age = 30
org = 'varaha'
msg = f'{name} is working in {org}'
print(msg)
# end
# #### using dict in f-strings
# when using dict in fstring always use double quotes around dict elements in
# fstring
# start
d = {'name': 'vishnu', 'age': 30, 'org': 'varaha', 'loc': 'hyderabad'}
msg1 = f'{d["name"]} is working in {d["org"]}'
print(msg1)
