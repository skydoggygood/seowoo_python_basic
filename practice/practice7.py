#! /usr/bin/env python

lang0 = ["Python","JAVA"]
lang1 = ["C","C++","VB"]

#목표 : 두 리스트의 원소를 모두 포함하는 새로운 리스트 totalLang을 만들어 출력합니다. 

lang0.extend(lang1)

totalLang = lang0
print(totalLang)


#정답 
#totalLang = lang0 +lang1

