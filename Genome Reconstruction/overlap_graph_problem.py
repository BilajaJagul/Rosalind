#! /usr/bin/python

import sys

def overlap_graph(patterns):
    l_patterns = len(patterns)
    k = len(patterns[0])
    adjacency_matrix = [[1 if i!= j and patterns[i][1:] == patterns[j][0:k-1] else 0 for j in range(l_patterns)] for i in range(l_patterns)]
    return adjacency_matrix

with open(sys.argv[1],'r') as lh:
    patterns = []
    for line in lh:
        patterns.append(line[:-1])

patterns = sorted(patterns)
overlap_results = overlap_graph(patterns)
for j in range(len(overlap_results)):
    for k in range(len(overlap_results[j])):
        if overlap_results[j][k] == 1:
            print(r"{} -> {}".format(patterns[j], patterns[k]))


