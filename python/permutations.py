#!/usr/bin/python3
from itertools import permutations
st = 'ABC'
l = permutations(st)
for i in l:
    print("".join(i))
