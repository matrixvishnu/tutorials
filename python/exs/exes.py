#!/usr/bin/python3
import time


def str_comp(s1, s2):
    return s1.upper() == s2.upper()

def str_comp3(s1, s2):
    if len(s1) != len(s2):
        return False
    else:
        return s1.upper() == s2.upper()


def str_comp2(s1, s2):
    if len(s1) != len(s2):
        return False
    else:
        s1_c = iter(s1)
        s2_c = iter(s2)
        for i in range(len(s1)):
            if next(s1_c).upper() != next(s2_c).upper():
                return False
        return True


s1 = "Thisisaverybig_stringthathasmorethantwostrings"
s2 = "Thisisaverybig_stringthathasmorethantwostrings"
s3 = "Thisisaverybigstringhathasmorethantwostrings"

d1 = "Thisisaverybig_stringthathasmorethantwostrings"
d2 = "Thisisaverybig_stringthathasmorethantwostrings"
d3 = "Thisisaverybigstringhathasmorethantwostrings"

c1 = "Thisisaverybig_stringthathasmorethantwostrings"
c2 = "Thisisaverybig_stringthathasmorethantwostrings"
c3 = "Thisisaverybigstringhathasmorethantwostrings"

d={}
start_time1 = time.time()
for i in range(29):
    print(str_comp(s1, s2))
d['one_t'] = time.time()-start_time1

start_time1 = time.time()
for i in range(29):
    print(str_comp(s1, s3))
d['one_f'] = time.time()-start_time1

start_time1 = time.time()
for i in range(29):
    print(str_comp2(d1, d2))
d['two_t'] = time.time()-start_time1
start_time1 = time.time()
for i in range(29):
    print(str_comp2(d1, d3))
d['two_f'] = time.time()-start_time1


start_time1 = time.time()
for i in range(29):
    print(str_comp3(c1, c2))
d['three_t'] = time.time()-start_time1

start_time1 = time.time()
for i in range(29):
    print(str_comp3(c1, c3))
d['three_f'] = time.time()-start_time1
print(d)
for k in d:
    print(k,d[k])
