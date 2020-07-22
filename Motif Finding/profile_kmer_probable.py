#! /usr/bin/python

import sys

def profile_kmer(text, k, p_matrix):
    l_text = len(text)
    probable_pattern = []
    score = -float("inf")
    for j in range(l_text - k + 1):
        pattern = text[j:j+k]
        local_score = 1
        for i in range(len(pattern)):
            #print(p_matrix[pattern[i]][i])
            local_score *= p_matrix[pattern[i]][i]
        if local_score > score:
            score = local_score
            probable_pattern = [pattern]
        elif local_score == score:
            probable_pattern.append(pattern)
    return probable_pattern

with open(sys.argv[1],'r') as lh:
    i = 0
    profile = []
    for line in lh:
        i = i + 1
        if i == 1:
            text = line[:-1]
        elif i == 2:
            k = int(line)
            print(k)
        else:
            profile.append(line)
    profile = [[float(i) for i in prof.split(" ")] for prof in profile]
    #print(profile)
    profile_matrix = {k:v for k, v in zip(['A','C','G','T'],profile)}
    #print(profile_matrix)
    print(profile_kmer(text, k, profile_matrix))


