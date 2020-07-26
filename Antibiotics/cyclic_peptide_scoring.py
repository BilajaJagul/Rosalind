#! /usr/bin/python

import os, sys

with open(sys.argv[1],'r') as lh:
    amino_acid_weights = {}
    for line in lh:
        data = line[:-1].split(" ")
        amino_acid_weights[data[0]] = data[1]


def cyclic_spectrum(peptide):
    l_peptide = len(peptide)
    prefix_mass = [0]
    for j in range(l_peptide):
        prefix_mass += [prefix_mass[-1] + int(amino_acid_weights[peptide[j]])]

    full_mass = prefix_mass[l_peptide]

    peptide_counts = {str(0):1}

    for j in range(0, l_peptide):
        for i in range(j+1, l_peptide + 1):
            linear_peptide = prefix_mass[i] - prefix_mass[j]
            if peptide_counts.get(str(linear_peptide)):
                peptide_counts[str(linear_peptide)] += 1
            else:
                peptide_counts[str(linear_peptide)] = 1
            if j > 0 and i < l_peptide:
                cyclic_peptide = full_mass - (prefix_mass[i] - prefix_mass[j])
                if peptide_counts.get(str(cyclic_peptide)):
                    peptide_counts[str(cyclic_peptide)] += 1
                else:
                    peptide_counts[str(cyclic_peptide)] = 1

    return peptide_counts

def scoring(peptide, compare_spectrum):
    peptide_counts = cyclic_spectrum(peptide)
    #print(compare_spectrum)
    score = 0
    for j in range(len(compare_spectrum)):
        if peptide_counts.get(compare_spectrum[j]):
            peptide_counts[compare_spectrum[j]] -= 1
            if peptide_counts[compare_spectrum[j]] >= 0:
                score += 1
    return score
        

with open(sys.argv[2], 'r') as lh:
    i = 0
    for line in lh:
        i = i + 1
        if i == 1:
            peptide = line[:-1]
        else:
            spectrum = line[:-1].split(" ")

print(scoring(peptide, spectrum))



