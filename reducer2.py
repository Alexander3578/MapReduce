#!/usr/bin/env python3
# -*-coding:utf-8 -*
 
import sys
 
counter = 0
sum = 0
for line in sys.stdin:
    counter += 1
    line = line.strip()
    num, _ = line.split('=', 1)
    sum += int(num)
 
print(sum / counter)
