#! /usr/bin/python

import sys

def pattern_count(text, pattern):
    pattern_length = len(pattern)
    text_length = len(text)
    if text_length < pattern_length or text_length == 0 or pattern_length == 0:
        return 0
    count = 0
    for j in range(0, text_length - pattern_length):
        if text[j:j+pattern_length] == pattern:
            count = count + 1
    return count


print(pattern_count(sys.argv[1], sys.argv[2]))

