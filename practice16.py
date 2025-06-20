#! /usr/bin/env python

#sample_dataset = "We tried list and we tried dicts also we tried Zen"

#word_list = sample_dataset.split(' ')

#for word in word_list: 
#    count = word_list.count(word)
#    print(f'{word} {count}')


s = "We tried list and we tried dicts also we tried Zen"

word_list = {'word':s.split()}

print(word_list)

seen = []

for word in word_list['word']:
    if word not in seen:
        count = word_list['word'].count(word)
        print(f'{word} {count}')
        seen.append(word)   

