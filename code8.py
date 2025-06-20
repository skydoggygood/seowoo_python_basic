#! /usr/bin/env python

fruit_1 = 'apple'
fruit_2 = 'peach'

num_fruit = 3 

print(fruit_1)
print(fruit_2)

print('{} tree'.format(fruit_1))
print(f'{fruit_1} tree')
print(f'{fruit_1} {fruit_2} tree')
print('{} {} tree'.format(fruit_1, fruit_2))

print('{1} {0} {1} {1} tree'.format(fruit_1,fruit_2))


