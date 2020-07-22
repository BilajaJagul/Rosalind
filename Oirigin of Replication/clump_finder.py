#! /bin/usr/python

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
    return ""+number_to_pattern(number // 4, k-1) + mapping[number % 4]

def freq(sequence, k):
    l_seq = len(sequence)
    frequency = [0 for j in range(0, 4**k)]
    max_count = 0
    max_numbers = []
    for j in range(0, l_seq - k + 1):
        number = pattern_to_number(sequence[j:j+k])
        frequency[number] = frequency[number]  + 1
    return frequency

def clum_freq(genome,k,t,L):
    l_genome = len(genome)
    clump = [0 for j in range(0, 4 ** k)]
    first_sequence = genome[0:L]
    kmer_freq = freq(first_sequence, k)
    for j in range(0, len(kmer_freq)):
        if kmer_freq[j] >= t:
            clump[j] = 1
    for i in range(1, l_genome - L + 1):
        latest_sequence = pattern_to_number(genome[i+L-k:i+L])
        kmer_freq[latest_sequence] += 1
        if kmer_freq[latest_sequence] >= t:
            clump[latest_sequence] = 1
    frequent_sequences = []
    for l in range(0, len(clump)):
        if clump[l] == 1:
            frequent_sequences.append(number_to_pattern(l,k))
    return frequent_sequences

print(clum_freq(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])))


