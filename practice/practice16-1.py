#! /usr/bin/env python

s = 'We tried list and we tried dicts also we tried Zen'

print(s.split()) #공백 기준으로 문자열 쪼개서 리스트로 만들기
s_spl = s.split() #쪼갠 변수는 s_spl에 저장

cnt_dict = {} #단어의 등장 횟수를 지정할 빈 딕셔너리 만들기
print(cnt_dict)
print(cnt_dict.keys()) #딕셔너리의 키요소

# 처음 만났을 때
#cnt_dict[s_spl[0]] = 1 #'We'가 나올거임

# 같은 key가 또 나왔을 때
#cnt_dict[s_spl[0]] += 1 #만약에 문자열에서 또 나오면 1 더해라

for i in s_spl:
    if i not in cnt_dict:
        cnt_dict[i] = 1 
    else:
        cnt_dict[i] += 1

for word in cnt_dict:
    print(f"{word} : {cnt_dict[word]}")

#{'We': 3, 'tred': 3} 최종적으로 만들고자 하는 형태


#cnt_dict에 key가 있는지 확인하는 코드 (bool,T or F) 
#print('We' in cnt_dict)

#for i in s_spl: 
#    print(f'{i} cnt_dict에 있어요? {i in cnt_dict}')
#    if i in cnt_dict:
#        print("있음!")
#    else:
#        print("없음!")  

