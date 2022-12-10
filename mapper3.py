#!/usr/bin/env python3
# -*-coding:utf-8 -*
 
import sys
import re
 
marks = """#();,:„“"'»–«"""
marks_end = ".!?…"
prev_tokens = []
 
for line in sys.stdin:
    tokens = re.findall( r'\w+|[^\s\w]+', line)
    tokens, prev_tokens = (prev_tokens + tokens, tokens)
    marks_counter = 0
    for token in tokens:
        if token in marks_end:
            print("%s=%s" % (token, marks_counter))
            marks_counter = 0
        elif token in marks:
            marks_counter += 1
