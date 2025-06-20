#! /usr/bin/env python

total = 100 #처음 시작 숫자
result = 0 #홀수를 저장해둘 공간 

while total <= 200: #시작 숫자가 200이 되기 전까지
    if total % 2 == 1: #만약에 total 변수를 2로 나눴는데 1이야? -> 홀수야?
        result += total # result라는 저장소에 홀수인 total 숫자를 하나씩 더해놔
    total += 1 #처음 숫자에서 (100)에서 1씩 계속 더해 

print(result) #100-200 사이에 홀수 숫자 다 더해

#강사님 정답
#result = 0 (시작값은 0)

#for i in range(100,201): (범위는 100에서 200까지인 변수 i가 있다)
    #if i % 2 == 0: (i를2로 나눠서 나머지0이면 짝수)
        #짝수
        #continue (계속해)
    #print(i) (짝수면 건너뛰었을 거니까  남은거 홀수들 밖에 없지? 그것들 보여줘봐) 
    #result_list.append(i) #어떤 홀수가 들어있는지 한번 봐보자
    #result += i (홀수로 나온 애들 i라는 변수저장소에 다 더해놔) 
#print(result) (결과값 내와봐) 


