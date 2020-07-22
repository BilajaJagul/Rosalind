#! /usr/bin/python

import sys
import random

def profile(n, motifs):
    prof = {'A':[0 for i in range(k)],'C':[0 for i in range(k)],'G':[0 for i in range(k)], 'T':[0 for i in range(k)]}
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

def gibbs_sampler(k, t, N, DNA):
    j = 0
    best_motif_score = float("inf")
    while j < 2000:
        local_motif = []
        for dna in DNA:
            random_start = random.randint(0, len(dna)-k)
            local_motif.append(dna[random_start:random_start+k])
        best_motif = local_motif
        best_score = score(best_motif)
        for i in range(0, N):
            pick = random.randint(0, t-1)
            #print(local_motif)
            profile_one_left = profile(t-1, [local_motif[l] for l in range(0, len(local_motif)) if l != pick])
            motif_pick = profile_kmer(DNA[pick], k, profile_one_left)
            local_motif[pick] = motif_pick
            #print(local_motif)
            local_score = score(local_motif)
            if local_score < best_score:
                best_score = local_score
                best_motif = local_motif
        if best_score < best_motif_score:
            best_overall_motif = best_motif
            best_motif_score = best_score
        j = j + 1
    return best_overall_motif

with open(sys.argv[1],'r') as lh:
    i = 0
    DNA = []
    for line in lh:
        i = i + 1
        if i == 1:
            line = line[:-1]
            t1 = line.split(" ")
            k = int(t1[0])
            t = int(t1[1])
            N = int(t1[2])
        else:
            DNA.append(line[:-1])

print(gibbs_sampler(k,t,N,DNA))

