#! /usr/bin/env python

exch = {환율정보}

input_money = input('Money: ') 
list_money = input_money.split(', ')
print(list_money[0].split()[0]) #10
print(list_money[0].split()[1]) #USD

print(exch[list_money[0].split()[1]]) #exch[USD] -> 1203.83
print()
print(int(list_money[0].split()[0]) * exch[list_money[0].split()[1]]) #first part

print(inst(list_money[0].split()[0]) * exch[list_money[0].
