#! /usr/bin/python

import os, sys

def spectral_conv(spectrum):
    peptide_count = {}
    for j in spectrum:
        for i in spectrum:
            diff = int(i) - int(j)
            if diff > 0:
                if peptide_count.get(str(diff)):
                    peptide_count[str(diff)] += 1
                else:
                    peptide_count[str(diff)] = 1

    peptide_sorted_count = sorted(peptide_count, reverse = True, key = peptide_count.get)
    result = ""
    #print(peptide_count)
    for peptide in peptide_sorted_count:
        result += (peptide + " ") * peptide_count[peptide]

    return result

with open(sys.argv[1],'r') as lh:
    spectrum = []
    for line in lh:
        spectrum += line[:-1].split(" ")

print(spectral_conv(spectrum))
