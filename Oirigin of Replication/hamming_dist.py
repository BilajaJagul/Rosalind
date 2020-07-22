#! /bin/usr/python

import sys

def hamming_d(pattern1, pattern2):
    return len([k for k,j in zip(pattern1, pattern2)if k != j])

print(hamming_d(sys.argv[1], sys.argv[2]))
