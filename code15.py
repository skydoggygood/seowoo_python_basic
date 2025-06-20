#! /usr/bin/env python

a = {2,4,6,8,10,12}
b = {3,6,9,12}
print('a:',a,'\nb:',b)
print(a|b)
print(set.union(a,b))
print(a&b)
print(set.intersection(a,b))
print(a^b)
print(set.symmetric_difference(a,b))
print()
a |= {100} #a=a|{100}
print(a)
a.update({200})
print(a)
a.add(1000)
print(a)
a.remove(200)
print(a)

