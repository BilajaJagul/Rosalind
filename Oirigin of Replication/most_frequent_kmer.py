#! /usr/bin/python

import sys

def kmer_count(text, k):
    text_length = len(text)
    if text_length == 0:
        return 0
    kmer_dict = {}
    kmer_max = []
    max_val = 0
    count = 0
    for j in range(0, text_length - k):
        kmer = text[j:j+k]
        count = 0
        for i in range(0, text_length - k):
            if text[i:i+k] == kmer:
                count = count + 1
        if count > max_val:
            max_val = count;
            kmer_max = []
            kmer_max.append(kmer)
        elif count == max_val and kmer not in kmer_max:
            kmer_max.append(kmer)
    return kmer_max

print(kmer_count(sys.argv[1], int(sys.argv[2])))

