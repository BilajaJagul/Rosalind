#! /usr/bin/python

import sys

def rev_complement(strand):
    mapping = {'A':'T','C':'G','G':'C','T':'A'}
    complement = [mapping[i] for i in strand] 
    rev_complement = complement[::-1]
    rev_complement_together = ""
    for j in rev_complement:
        rev_complement_together += j
    return rev_complement_together

print(rev_complement(sys.argv[1]))
