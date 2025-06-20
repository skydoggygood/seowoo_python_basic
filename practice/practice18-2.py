#! /usr/bin/env python

list_fibo = [0, 1]
  
def fibonacci(n):
    for i in range(n):
        list_fibo.append(list_fibo[-1]+list_fibo[-2])
    return list_fibo[n-1]
  
n=int(input('n? '))
print(fibonacci(n))

