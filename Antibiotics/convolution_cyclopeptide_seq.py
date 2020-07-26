#! /usr/bin/python

import os, sys

def linear_spectrum(peptide):
    peptide = peptide.strip("0")
    l_pep = len(peptide)
    prefix_mass = [0]
    j = 0
    l_peptide = 0
    while j < l_pep:
        if amino_acid_weights.get(peptide[j:j+3]):
            prefix_mass += [prefix_mass[-1] + int(amino_acid_weights[peptide[j:j+3]])]
            j = j + 3
            l_peptide += 1
        elif amino_acid_weights.get(peptide[j:j+2]):
            prefix_mass += [prefix_mass[-1] + int(amino_acid_weights[peptide[j:j+2]])]
            j = j + 2
            l_peptide += 1
        else:
            break
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
    l_peptide = len(peptide_1)
    j = 0
    mass = 0
    while j < l_peptide:
        if amino_acid_weights.get(peptide_1[j:j+3]):
            mass += int(amino_acid_weights[peptide_1[j:j+3]])
            j = j + 3
        elif amino_acid_weights.get(peptide_1[j:j+2]):
            mass += int(amino_acid_weights[peptide_1[j:j+2]])
            j = j + 2
        else:
            return mass
    return mass

def cyclic_spectrum(peptide_2):
    peptide_2 = peptide_2.strip("0")
    l_pep = len(peptide_2)
    prefix_mass = [0]
    l_peptide = 0
    j = 0
    while j < l_pep:
        if amino_acid_weights.get(peptide_2[j:j+3]):
            prefix_mass += [prefix_mass[-1] + int(amino_acid_weights[peptide_2[j:j+3]])]
            j = j + 3
            l_peptide += 1
        elif amino_acid_weights.get(peptide_2[j:j+2]):
            prefix_mass += [prefix_mass[-1] + int(amino_acid_weights[peptide_2[j:j+2]])]
            j = j + 2
            l_peptide += 1
        else:
            break

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


def spectral_conv(spectrum, M):
    peptide_count = {}
    for j in spectrum:
        for i in spectrum:
            diff = int(i) - int(j)
            if diff > 57 and diff < 200:
                if peptide_count.get(str(diff)):
                    peptide_count[str(diff)] += 1
                else:
                    peptide_count[str(diff)] = 1

    peptide_sorted_count = sorted(peptide_count, reverse = True, key = peptide_count.get)
    if len(peptide_sorted_count) < M:
        amino_acids = peptide_sorted_count
    else:
        amino_acids = peptide_sorted_count[:M]
    for peptide in range(M, len(peptide_sorted_count)):
        if peptide_count[peptide_sorted_count[peptide]] >= peptide_count[str(amino_acids[M-1])]:
            amino_acids.append(peptide_sorted_count[peptide])

    #result = ""
    #print(peptide_count)
    #for peptide in peptide_sorted_count:
    #    result += (peptide + " ") * peptide_count[peptide]

    amino_acid_weights = {}

    for aa in amino_acids:
        amino_acid_weights[aa] = int(aa)

    return amino_acid_weights


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


with open(sys.argv[1],'r') as lh:
    i = 0
    exp_spectrum = []
    for line in lh:
        i = i + 1
        if i == 1:
            M = int(line[:-1])
        elif i == 2:
            N = int(line[:-1])
        else:
            exp_spectrum += line[:-1].split(" ")

amino_acid_weights = spectral_conv(exp_spectrum, M)
amino_acids = list(amino_acid_weights.keys())
result = leaderboard_cyclopeptide(exp_spectrum, N)

j = 0
output = ""
while j < len(result):
    if amino_acid_weights.get(result[j:j+3]):
        output += result[j:j+3] + "-"
        j = j + 3
    elif amino_acid_weights.get(result[j:j+2]):
        output += result[j:j+2] + "-"
        j = j + 2
    else:
        break

print(output[:-1])


