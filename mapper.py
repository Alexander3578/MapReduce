#!/usr/bin/env python3
# -*-coding:utf-8 -*
 
import sys
import re
 
text = sys.stdin.read()
tokens = re.split(r'[.…!?]+', text)
 
for token in tokens:
    if token != "":
        token = token.replace("\n", " ")
        token.strip()
        print('%s=%s' % (token, token.count(" ") + 1))
