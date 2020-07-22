#! /bin/usr/python

import sys

def min_skew(pattern):
    l_pattern = len(pattern)
    skew = [0 for i in range(0, l_pattern+1)]
    mapping = {'A':0,'G':1,'C':-1,'T':0}
    min_score = l_pattern
    min_positions = []
    for j in range(1, len(skew)):
        skew[j] = skew[j-1] + mapping[pattern[j-1]]
        if skew[j] < min_score:
            min_score = skew[j]
            min_positions = [j]
        elif skew[j] == min_score:
            min_positions.append(j)
    return min_positions


with open(sys.argv[1], 'r') as lh:
    sequence = ""
    for line in lh:
        sequence += line[:-1]

print(min_skew(sequence))
