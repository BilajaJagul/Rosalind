#! /usr/bin/python

import sys
import random

def profile(n, prof, motif):
    for nucleotide in prof:
        if n == 1:
            break
        else:
            prof[nucleotide] = [(n + 3) * i - 1 for i in prof[nucleotide]]
    for j in range(len(motif)):
        prof[motif[j]][j] += 1
    for nucleotide in prof:
        prof[nucleotide] = [(i+1)/(n+5) for i in prof[nucleotide]]
    #print(prof)
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
            probable_pattern = [pattern]
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

def greedy(k, t, DNA):
    prof = {'A':[0 for i in range(k)],'C':[0 for i in range(k)],'G':[0 for i in range(k)], 'T':[0 for i in range(k)]}
    best_motifs = []
    for dna in range(len(DNA)):
        best_motifs.append(DNA[dna][0:k])
    score_best_motifs = score(best_motifs)
    for j in range(len(DNA[0])-k+1):
        motif1 = DNA[0][j:j+k]
        local_motifs = [motif1]
        prof_subset = prof
        for i in range(1, t):
            prof_subset = profile(i, prof_subset, local_motifs[-1])
            #print(prof_subset)
            patterns = profile_kmer(DNA[i], k, prof_subset)
            #print(patterns)
            local_motifs.append(patterns[0])
        local_motif_score = score(local_motifs)
        if local_motif_score < score_best_motifs:
            best_motifs = local_motifs
            score_best_motifs = local_motif_score
    return best_motifs

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

print(greedy(k,t,DNA))


