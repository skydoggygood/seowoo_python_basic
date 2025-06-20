#! /usr/bin/env python

#주어진 주민등록번호:
# regNum0 = "951213-0000000"
# regNum1 = "960125-0000000"
# regNum2 = ("970705-0000000"
# 목표: 주민등록번호에서 월과 일을 추출하여 영어 약자로 변환한 후, 특정 형식으로 출력합니다.
# 예: regNum0: Dec-13

regNum0 = "951213-0000000"
regNum1 = "960125-0000000"
regNum2 = "970705-0000000" 

month0 = regNum0[2:4]
month1 = regNum1[2:4]
month2 = regNum2[2:4]

day0 = regNum0[4:6]
day1 = regNum1[4:6]
day2 = regNum2[4:6]

monthname = {'12' : 'DEC', '01' : 'JAN', '07' : 'JUL'}

print("regNum0: ",monthname[month0],"-",day0, sep = '')

print("regNum1: ",monthname[month1],"-",day1, sep = '')

print("regNum2: ",monthname[month2],"-",day2, sep = '')

#print() 사용할 시에 공백 생기는거 해결법

#1. 다 붙여버리고 한번에 print

#2. print 설정 중sep 설정을 바까요 (기본값 빈칸(space))


#강사님 정답
#d_month_int={1:'jan',2:'Feb',3:'Mar',7;'jul',12:'dec'}
#d_month_str={'01':'jan','02':'Feb','03':'Mar','07':'jul','12':'dec'}

#print(d_month_int)
#print(d_month_str)
#print(d_month_int[1])
#print(d_month_str['01'])

#regNum0 = '951213-0000000'
#regNum1 = '960125-0000000'
#regNum2 = '970705-0000000'
#print(int(regNum1[2:4])
#print(regNum1[2:4])

#d_person0 = {'Mon': d_month_str[regNum0[2:4], 'Day': regNum0[4:6]}
#d_person1 = {'Mon': d_month_str[regNum1[2:4], 'Day': regNum1[4:6]}
#d_person2 = {'Mon': d_month_str[regNum2[2:4], 'Day': regNum2[4:6]}

#print(f"regNum0: {d_person0['Mon'}-{d_person0['Day'}")
#print(f"regNum1: {d_person1['Mon'}-{d_person1['Day'}")
#print(f"regNum2: {d_person2['Mon'}-{d_person2['Day'}")
