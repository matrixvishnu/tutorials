#!/usr/bin/python
# In Python, functions are first-class objects.
# This means that functions can be passed around and used as arguments,
# just like any other object (string, int, float, list, and so on).
# Consider the following three functions:
def say_hello(name):
    return "Hello"+name


def be_awesome(name):
    return "Yo "+name+", together we are the awesomest!"


def greet(greeter_func, name):
    return greeter_func(name)


#print(greet(be_awesome, "vishnu"))
# The greet_bob() function however, expects a function as its argument.
# We can, for instance, pass it the say_hello() or the be_awesome() function
# Note that greet_bob(say_hello) refers to two functions, but in different ways:
# greet_bob() and say_hello. The say_hello function is named without parentheses.
# This means that only a reference to the function is passed.
# The function is not executed.
# The greet_bob() function, on the other hand, is written with parentheses,
# so it will be called as usual.

# Inner Functions

# It's possible to define functions inside other functions.
# Such functions are called inner functions.
# Here's an example of a function with two inner functions:

def parent(string):
    def first_child():
        return "this is first child"

    def second_child():
        return "this is secoend child"

    d = {'first_child':first_child, 'second_child':second_child }
    if string in d:
        return d[string]
    else:
        return "please give any of the following args "+d.values()



f=parent('first_child')
print f
print f()
# the inner functions are not defined until the parent function is called.
# They are locally scoped to parent():
# they only exist inside the parent() function as local variables.
# Try calling first_child(). You should get an error:
# first_child()

# Returning Functions From Functions

# Python also allows you to use functions as return values.
# The following example returns one of the inner functions from the outer parent()
# function:


