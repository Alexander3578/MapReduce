#!/usr/bin/env python3
# -*-coding:utf-8 -*
 
import sys
 
longest_sentences = []
longest_sentences_lenght = 0
for line in sys.stdin:
    line = line.strip()
    text, length = line.split('=', 1)
    length = int(length)
    if length == longest_sentences_lenght:
        longest_sentences.append(text)
    if length > longest_sentences_lenght:
        longest_sentences = [text]
        longest_sentences_lenght = length
 
print(longest_sentences_lenght)
for line in longest_sentences:
    print(line)