#! /usr/bin/python

import sys
import random

def profile(n, prof, motifs):
    for motif in motifs:
        for j in range(len(motif)):
            prof[motif[j]][j] += 1
    for nucleotide in prof:
        prof[nucleotide] = [(i+1)/(n+4) for i in prof[nucleotide]]
    return prof
    

def profile_kmer(text, k, p_matrix):
    l_text = len(text)
    probable_pattern = []
    score = -float("inf")
    for j in range(l_text - k + 1):
        pattern = text[j:j+k]
        local_score = 1
        for i in range(len(pattern)):
            local_score *= p_matrix[pattern[i]][i]
            #print(local_score)
        if local_score > score:
            score = local_score
            probable_pattern = pattern
    return probable_pattern

def score(motif_matrix):
    k = len(motif_matrix[0])
    t = len(motif_matrix)
    score_matrices = [[0,0,0,0] for j in range(k)]
    mapping = {'A':0,'C':1,'G':2,'T':3}
    for i in range(k):
        for j in motif_matrix:
            score_matrices[i][mapping[j[i]]] += 1
    score = 0
    for i in range(k):
        score += t - max(score_matrices[i])
    return score

def most_freq(array):
    #print(len(array))
    local_count = 1
    max_count = 0
    max_element = [array[0]]
    local_element = array[0]
    for j in range(1, len(array)):
        if local_element == array[j]:
            local_count += 1
        else:
            if local_count > max_count:
                max_count = local_count
                max_element = local_element
            local_count = 1
            local_element = array[j]
            print(max_count)
    return(max_element)

def partition(A, l, r):
    i = l
    for j in range(l, r):
        if A[j] < A[l]:
            i = i + 1
            A[i], A[j] = A[j], A[i]
    A[i], A[l] = A[l], A[i]
    return i

def quick_sort(A, l, r):
    if l >= r:
        return
    k = random.randint(l, r-1)
    A[k],A[l] = A[l], A[k]
    m = partition(A, l, r)
    quick_sort(A, l, m)
    quick_sort(A, m+1, r)
    return A

def randomized(k, t, DNA):
    prof = {'A':[0 for i in range(k)],'C':[0 for i in range(k)],'G':[0 for i in range(k)], 'T':[0 for i in range(k)]}
    i = 0
    best_score_overall = float('inf')
    while i < 2000:
        best_motifs = []
        for dna in range(len(DNA)):
            random_start = random.randint(0, len(DNA[dna]) - k)
            best_motifs.append(DNA[dna][random_start: random_start + k])
        score_best_motifs = score(best_motifs)
        flag = True
        while flag:
            local_subset = []
            prof_subset = profile(t, prof, best_motifs)
            for dna in DNA:
                local_subset.append(profile_kmer(dna, k, prof_subset))
            local_motif_score = score(local_subset)
            if local_motif_score <= score_best_motifs:
                best_motifs = local_subset
                score_best_motifs = local_motif_score
            else:
                if score_best_motifs <= best_score_overall:
                    best_motifs_overall = best_motifs
                    best_score_overall = score_best_motifs
                flag = False
        i = i + 1
    return best_motifs_overall

with open(sys.argv[1],'r') as lh:
    i = 0
    DNA = []
    for line in lh:
        i = i + 1
        if i == 1:
            t = line.split(" ")
            k = int(t[0])
            t = int(t[1])
        else:
            DNA.append(line[:-1])

print(len(DNA))
print(randomized(k,t,DNA))

