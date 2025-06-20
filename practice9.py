#! /usr/bin/env python

sample_dataset = "We tried list and we tried dicts also we tried Zen" 

word_list = sample_dataset.split(' ') #공백을 기준으로 단어 나누기

seen = [] #이미 출력한 단어들을 이 리스트에 저장

for word in word_list: #word_list안에 있는 word를 하나씩 꺼내서..
    if word not in seen: #만약 word가 seen안에 없으면 
        count = word_list.count(word) #count라는 저장소에 word_list안에서 word가 몇번 나왔는지 센다
        print(f'{word} {count}') #{단어} {갯수} 순으로 출력한다
        seen.append(word) #이미 출력한 단어는 seen에 추가하기 (다음에 중복 출력 안되게) 

