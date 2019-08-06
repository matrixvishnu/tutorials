#!/usr/bin/python3
def rev(st):
    if len(st) == 1:
        return st
    else:
        return st[-1]+rev(st[:-1])

print(rev("vishnu"))

def missing(l1,l2):
    return set(l1)-set(l2)
print(missing([1,2,4,5,6],[1,2,4,6]))

def missing1(l3):
    if l3[-1]-l3[-2] >1:
        return l3[-1] -1
    else:
        l3.pop()
        return missing1(l3)
print(missing1([1,2,4,5]))
