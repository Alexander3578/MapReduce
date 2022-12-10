#!/usr/bin/env python3
# -*-coding:utf-8 -*
 
import sys
 
 
sentence_counter = 0
text_length = 0
for line in sys.stdin:
    sentence_counter += 1
    line = line.strip()
    _, length = line.split('=', 1)
    text_length += int(length)
 
print(text_length / sentence_counter)