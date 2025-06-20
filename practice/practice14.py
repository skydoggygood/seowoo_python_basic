#! /usr/bin/env python


num = int(input("무슨 단을 가져올까요?:"))

if 2 <= num <= 19:
    for i in range(1,20):
        print(num*i)
    
else:
    print("숫자를 다시 입력하세요.")

#강사님 정답

#input_gugu=input("gugu") #숫자? 문자? 큰수?

#1.숫자인지 확인
#2.True만 크기비교가능. 크기비교

#while not input_gugu.isdigit(): #숫자면 True, 아니면 False. 아니면 다시 받아야함. 제대로 받을때까지 묻기
#   print(f'input_gugu is not digit. {input_gugu}')
#   input_gugu=input('gugu?') #숫자?문자?큰수?
#print(f'input_gugu is digit! {input_gugu}')

#for i in range(2,20):
#   print(f'{input_gugu} * {1} = {int(input_gugu)*i}')

