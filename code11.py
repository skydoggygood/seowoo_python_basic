#sdasdasdasd! /usr/bin/env python

num = [1,2,3,4] 
print(num)
num[1]=6
print(num)
del num[2:]
print(num)

num.append(3)
print('append   3   :', num)
num.append([1,2])
print('append   [1][2]:', num)
num.remove([1,2])
print(num)
num.sort()
a = num.sort()
print(a)
print(num)

print(num)
num.reverse()
print(num)
b = num.reverse()
print(b)
print(num) 
