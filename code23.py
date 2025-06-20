#! /usr/bin/env python

count = 0 
while count <10:
    count+=1 
    if count % 2 == 0:
        continue
    print("Odd number:",count)

