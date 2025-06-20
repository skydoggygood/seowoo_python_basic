#! /usr/bin/env python

#함수를 이용해 피보나치 수영을 계산하세요
#F0 = 0
#F1 = 1 
#F2 = F0 + F2
#    = 0 + 1 
#    = 1

#목표 :F8 구하기 / 함수 fibonacci를 작성할 것 

#result0 = 0 
#print(result0)
#result1 = 0 + 1
#print(result1)
#result2 = result0 + result1
#print(result2)
#result3 = result1 + result2
#print(result3)
#result4 = result2 + result3
#print(result4)

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else: 
        return fibonacci(n-1) + fibonacci(n-2)

n = int(input("숫자를 입력하세요 (숫자항의 피보나치 수열)>>>"))
print(f"{fibonacci(n-1)}")
