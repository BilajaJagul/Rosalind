#! /bin/usr/python

import sys

def pattern_to_number(pattern):
    mapping = {'A':0,'C':1,'G':2,'T':3}
    if not pattern:
        return 0
    return 4 * pattern_to_number(pattern[:-1]) + mapping[pattern[-1]]

def freq(sequence, k):
    l_seq = len(sequence)
    frequency = [0 for j in range(0, 4**k)]
    max_count = 0
    max_numbers = []
    for j in range(0, l_seq - k + 1):
        number = pattern_to_number(sequence[j:j+k])
        frequency[number] = frequency[number]  + 1
        if max_count <  frequency[number]:
            max_count = frequency[number]
            max_numbers = [number]
        elif max_count == frequency[number]:
            max_numbers.append(number)
    return max_numbers

print(freq(sys.argv[1], int(sys.argv[2])))



