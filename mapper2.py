#!/usr/bin/env python3
# -*-coding:utf-8 -*
 
import sys
import re
 
words_row = []
counter = 0
unic_words = 0
for line in sys.stdin:
    words = re.split(r'[ ]|[^\s\w]+', line)
 
    for word in words:
        word = word.strip()
        if word != "":
            counter += 1
            word = word.lower()
            if word not in words_row:
                unic_words += 1
                words_row.append(word)
            if counter == 1000:
                counter = 0
                print("%s=%s" % (unic_words, 1))
                unic_words = 0
                words_row = []
