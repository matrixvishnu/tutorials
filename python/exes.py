#!/usr/bin/python3
from collections import Counter
import numpy as np
l = [1, 2, 3, 4, 4, 5, 6, 6, 7]
l3 = [11, 22, 33]
print(l+l3)
s = set(l)
print(s)
l2 = list(s)
print(l2)
l1 = np.array(l)
l2 = np.array(l2)
print(l1-l2)
c1 = Counter(l)
c2 = Counter(l2)
print(c1)
print(c2)
diff = c1-c2
print(diff)
print(list(diff.elements()))
