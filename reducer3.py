#!/usr/bin/env python3
# -*-coding:utf-8 -*
 
import sys
 
counter = 0
marks_count = 0
for line in sys.stdin:
    line = line.strip()
    _, num = line.split("=")
    marks_count += int(num)
    counter += 1
 
print(marks_count / counter)
