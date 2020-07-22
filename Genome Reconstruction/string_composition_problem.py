#! /usr/bin/python

import sys

def kmer_splitter(k, genome):
    sorted_kmers = []
    for j in range(len(genome) - k + 1):
        new_kmer = genome[j:j+k]
        l = len(sorted_kmers)
        if l >= 1:
            for i in range(len(sorted_kmers)):
                if sorted_kmers[i] < new_kmer:
                    continue
                sorted_kmers.insert(i, new_kmer)
                break
            if l == len(sorted_kmers):
                sorted_kmers.append(new_kmer)
        else:
            sorted_kmers.append(new_kmer)
    return sorted_kmers

with open(sys.argv[1],'r') as lh:
    i = 0
    DNA = ""
    for line in lh:
        i = i + 1
        if i == 1:
            k = int(line)
        else:
            DNA += line

result_kmers = kmer_splitter(k, DNA[:-1])
for j in result_kmers:
    print(j)


