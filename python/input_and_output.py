#!/usr/bin/python3
# ### input and output
# #### input
# in python input() will take input from user until input() instruction program
# executes normally input() asks user to enter values
# input will take entered values as is
# start
x = int(input('enter the values : '))
# end
# in the above code if we enter a string with out quotes we will get error
# #### raw_input()
# raw_input will convert any entered value to string
# start
y = int(input('enter the values : '))
# end
# in the above code what ever we enter it will not throw any error
# #### out put
# str.format() to format output in Python
# start
print('x is {0} and y is {1}'.format(x, y))
# end
# display the number in the hex or oct or binary format
# {0:b} --> binary {0:x} --> hexadecimal {0:o} --> octal
# start
print('x binary {0:b} and y hexadecimal {1:x}'.format(x, y))
# end
# ####Output String justification
# str.rjust(),   str.ljust() and str.center() to justify text output
# on screen and console.
# start
text = input("Enter String: ")
print("Left justification", text.ljust(60, "*"))
print("Right justification", text.rjust(60, "*"))
print("Center justification", text.center(60, "*"))
# end
