#! /usr/bin/python

import sys

def pattern_to_number(pattern):
    mapping = {'A':0,'C':1,'G':2,'T':3}
    if not pattern:
        return 0
    return 4 * pattern_to_number(pattern[:-1]) + mapping[pattern[-1]]

def number_to_pattern(number, k):
    mapping = ['A','C','G','T']
    if k == 1:
        return mapping[number]
    return "" + number_to_pattern(number // 4, k - 1) + mapping[number % 4]

def hamming_d(pattern1, pattern2):
    return len([i for i,j in zip(pattern1, pattern2) if i != j ])

def neighbors(pattern, d):
    if d == 0:
        return [pattern]
    if len(pattern) <= 1:
        return ['A','C','G','T']

    nearest_neighbors = neighbors(pattern[1:], d)
    neighborhood = []
    for neighbor in nearest_neighbors:
        if hamming_d(neighbor, pattern[1:]) < d:
            neighborhood += [x+neighbor for x in ['A','C','G','T']]
        else:
            neighborhood += [pattern[0] + neighbor]
    return neighborhood

def motif(k, d, DNA):
    freq_patterns = [0 for j in range(4 ** k)]
    l_DNA = len(DNA)
    for dna in DNA:
        l_dna = len(dna)
        local_freq = [0 for j in range(4 ** k)]
        for j in range(l_dna - k + 1):
            current_pat = dna[j : j + k]
            neighbors_pat = neighbors(current_pat, d)
            for neighbor in neighbors_pat:
                local_freq[pattern_to_number(neighbor)] += 1
        for j in range(4 ** k):
            if local_freq[j] > 0:
                freq_patterns[j] += 1
    patterns = []
    for t in range(4 ** k):
        if freq_patterns[t] >= l_DNA:
            patterns.append(number_to_pattern(t,k))
    return patterns

print(motif(int(sys.argv[1]), int(sys.argv[2]), sys.argv[3:]))


            
