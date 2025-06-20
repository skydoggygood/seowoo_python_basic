#! /usr/bin/env python

 #주어진 점수 범위와 학점:
 #90 ~ 100: A
 #80 ~ 89: B
 #70 ~ 79: C
 #60 ~ 69: D
 #~59: F
 #목표:
 #입력된 점수에 따라 해당하는 학점을 출력합니다.
 #입력: 95
 #출력: A
 #입력: 71
 #출력: C

score = int(input("성적 입력: "))

if score <= 100 and score >= 90:
    print("A") 
elif score <= 89 and score >= 80: 
    print("B")
elif score <=79 and score >= 70:
    print("C")
elif score <= 69 and score >= 60:
    print("D")
else: 
    print("F")


#강사님 정답

socre = int(input('input score:'))

if 90 <= score <= 100: 
    print("A") 
elif 80 <= score <= 89:
    print("B")
elif 70 <= score <= 79:
    print("C")
elif 60 <= score <= 69:
    print("D") 
else: 
    print("F")

