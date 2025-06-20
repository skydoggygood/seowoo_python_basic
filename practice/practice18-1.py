#! /usr/bin/env python

fibo = {0:0,1:1}

def fibonacci(n):
    if n in fibo:
        return fibo[n]
 
    fibo[n] = (fibonacci(n-1) + fibonacci(n-2))
    return fibo[n]
   
n = int(input("숫자를 입력하세요>>>"))
print(fibonacci(n-1))
