#! /usr/bin/env python

apple1 = {'price': 1000, 'color':'red', 'harvest': 'apple tree', 'price' : 2000}
print('\napple1:' , apple1)
print('apple1.keys():', apple1.keys())
print('apple1.values():',apple1.values())
print('apple1.items():',apple1.items())

print("\napple1.get('harvest'):",apple1.get('harvest'))

print()
print('price' in apple1)
print('color' in apple1)
print('fruit' in apple1)

apple1.clear()
print('\napple1:',apple1)                                       

