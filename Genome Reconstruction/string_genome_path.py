#! /usr/bin/python

import sys

def hamming_d(pattern1, pattern2):
    return len([k for k, j in zip(pattern1, pattern2) if k!=j])


def genome_path(patterns):
    l_pattern = len(patterns[0])
    l_patterns = len(patterns)
    k = 0
    for j in range(l_pattern):
        #print(hamming_d(patterns[0][j:l_pattern], patterns[1][0:l_pattern - j]))
        if hamming_d(patterns[0][j:l_pattern], patterns[1][0:l_pattern - j]) == 0:
            k = l_pattern - j
            break
    #print(k)
    final_pattern = patterns[0]
    for j in range(1, l_patterns):
        final_pattern += patterns[j][k:]
    return final_pattern


with open(sys.argv[1],'r') as lh:
    patterns = []
    for line in lh:
        patterns.append(line[:-1])

print(patterns)
print(genome_path(patterns))
