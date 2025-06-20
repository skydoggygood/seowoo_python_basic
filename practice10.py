#! /usr/bin/env python

#Operator & Statement
 #주어진 숫자:
 #num0 = 5
 #num1 = 7
 #목표:
 #두 숫자 중 더 큰 숫자를 출력합니다.
 #예: num0과 num1 중 더 큰 숫자는 7입니다. 

#num0 = 5
#num1 = 7

#if num0 > num1: 
#    print (int(num0))
#else :
#    print (int(num1)) 



num0 = input('input num0:')
num1 = input('input num1:')

print(type(num0))

if int(num0) < int(num1):
    print(f'num0과 num1 중 더 큰 숫자는 {num1}입니다')
elif int(num0) > int(num1): 
    print(f'num0과 num1 중 더 큰 숫자는 {num0}입니다')
else:
    print("똑같아요")

