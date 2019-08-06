import random
import math
import numpy as np
def swap(s):
    if len(s) == 1:
        return s
    else:
        s1 = s[random.randrange(0,len(s))]
        s2 = s.replace(s1,"")
    return s1+swap(s2)

print(swap('abcdef'))

d = {}

def fib(n):
    if n in d:
        f = d[n]
    if n <= 2:
        f = 1
    else:
        f = fib(n-1)+fib(n-2)
        d[n] = f
    return f
print(fib(10))

def fib1(n):
    if n == 0:
        return 1
    f = ((1.618034)**n-((-0.618034)**n))/math.sqrt(5)
    return round(f)
print(fib1(10))

for i in range(10):
    print("rec:"+str(fib(i))+", direct:"+str(fib1(i)))


