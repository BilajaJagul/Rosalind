#! /usr/bin/python

import os, sys

with open(sys.argv[1],'r') as lh:
    amino_acid_weights = {}
    for line in lh:
        data = line[:-1].split(" ")
        amino_acid_weights[data[0]] = data[1]
amino_acids = list(amino_acid_weights.keys())

def linear_spectrum(peptide):
    peptide = peptide.strip("0")
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
    return peptide_counts

def scoring(peptide, compare_spectrum):
    peptide_counts = linear_spectrum(peptide)
    #print(peptide_counts)
    #print(compare_spectrum)
    score = 0
    for j in range(len(compare_spectrum)):
        if peptide_counts.get(compare_spectrum[j]):
            peptide_counts[compare_spectrum[j]] -= 1
            if peptide_counts[compare_spectrum[j]] >= 0:
                score += 1
    return score

def trim(peptides, spectrum, N):
    #print(peptides)
    if not peptides:
        return []
    scored_peptides = []
    for peptide in peptides:
        scored_peptides.append((peptide, scoring(peptide, spectrum)))
    scored_peptides = sorted(scored_peptides,reverse = True, key = lambda x:x[1])
    if len(scored_peptides) < N:
        leaderboard_new = scored_peptides
    else:
        nth_score = scored_peptides[N-1][1]
        leaderboard_new = scored_peptides[:N]
        for position in range(N, len(scored_peptides)):
            if scored_peptides[position][1] == nth_score:
                leaderboard_new.append(scored_peptides[position])
    leaderboard_n = [j[0] for j in leaderboard_new]
    return leaderboard_n

def expand(peptides):
    expand_peptides = []
    for peptide in peptides:
        expand_peptides += [peptide + j for j in amino_acids]
    #print(expand_peptides)
    return expand_peptides

def mass(peptide_1):
    if len(peptide_1) == 1:
        return int(amino_acid_weights[peptide_1])
    return int(amino_acid_weights[peptide_1[-1]]) + mass(peptide_1[:-1])

def cyclic_spectrum(peptide_2):
    peptide_2 = peptide_2.strip("0")
    l_peptide = len(peptide_2)
    prefix_mass = [0]
    for j in range(l_peptide):
        prefix_mass += [prefix_mass[-1] + int(amino_acid_weights[peptide_2[j]])]

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

def cyclo_scoring(peptide, compare_spectrum):
    peptide_counts = cyclic_spectrum(peptide)
    #print(compare_spectrum)
    score = 0
    for j in range(len(compare_spectrum)):
        if peptide_counts.get(compare_spectrum[j]):
            peptide_counts[compare_spectrum[j]] -= 1
            if peptide_counts[compare_spectrum[j]] >= 0:
                score += 1
    return score



def leaderboard_cyclopeptide(ideal_spectrum, N):
    leaderboard = [""]
    leaderpeptide = "0"
    spectrum_sorted_number = sorted([int(j) for j in ideal_spectrum])
    parent_mass = spectrum_sorted_number[-1]
    #print(parent_mass)
    while len(leaderboard) > 0:
        #print(leaderboard)
        #print(parent_mass)
        new_leaderboard = []
        leaderboard = expand(leaderboard)
        for peptide in leaderboard:
            #print(peptide)
            peptide_mass = mass(peptide)
            #print(peptide)
            if peptide_mass == parent_mass:
                if cyclo_scoring(peptide, ideal_spectrum) > cyclo_scoring(leaderpeptide, ideal_spectrum):
                    leaderpeptide = peptide
            elif peptide_mass < parent_mass:
                new_leaderboard.append(peptide)
        leaderboard = new_leaderboard
        #print(len(leaderboard))
        #print("updated")
        leaderboard = trim(leaderboard, ideal_spectrum, N)
        #print(len(leaderboard))
    return leaderpeptide

#peptides = ['PVT','PTP','PTV','PCP','VPC','VTP','VCP','TPV','TPC','TVP']
#ideal_spectrum = ['0','97','97','99','101','103','196','198','198','200','202','295','297','299','299','301','394','396','398','400','400','497']

with open(sys.argv[2], 'r') as lh:
    i = 0
    for line in lh:
        i = i + 1
        if i == 1:
            N = int(line[:-1])
        else:
            input_spectrum = line[:-1].split(" ")

#print(N)
result = leaderboard_cyclopeptide(input_spectrum, N)
final_result = ''.join([amino_acid_weights[j] + "-" for j in result])

print(final_result[:-1])


