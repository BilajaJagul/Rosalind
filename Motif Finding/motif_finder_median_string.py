#! /usr/bin/python

import sys

def all_of_the_strings(k):
    if k == 1:
        return ['A','C','G','T']
    small_strings = all_of_the_strings(k-1)
    return [k + v for k in small_strings for v in ['A','C','G','T']]

def hamming_distance(pattern1, pattern2):
    return len([i for i, j in zip(pattern1, pattern2) if i != j])

def distance_pattern_strings(pattern, DNA):
    l_pat = len(pattern)
    distance = 0
    for dna in DNA:
        hamming_d = float('inf')
        for j in range(len(dna) - l_pat + 1):
            if hamming_d > hamming_distance(pattern, dna[j:j+l_pat]):
                hamming_d = hamming_distance(pattern, dna[j:j+l_pat])
        distance = distance + hamming_d
    return distance

def median_string(DNA, k):
    all_strings = all_of_the_strings(k)
    median_string = []
    min_d = float("inf")
    for string in all_strings:
        d = distance_pattern_strings(string, DNA)
        if min_d > d:
            min_d = d
            median_string = [string]
        elif min_d == d:
            median_string.append(string)
    return median_string

with open(sys.argv[1],'r') as fh:
    i = 0
    dna_val = []
    for line in fh:
        i = i + 1
        if i <= 1:
            k_val = int(line)
        else:
            dna_val.append(line)
print(median_string(dna_val, k_val))



