#! /usr/bin/python

import sys

def de_brujin(sequences):
    l_seq = len(sequences)
    k = len(sequences[0])
    adjacency_matrix = {}
    for j in range(l_seq):
        prefix = sequences[j][:k-1]
        suffix = sequences[j][1:k]
        if adjacency_matrix.get(prefix):
            if adjacency_matrix[prefix].get(suffix):
                adjacency_matrix[prefix][suffix] += 1
            else:
                adjacency_matrix[prefix][suffix] = 1
        else:
            adjacency_matrix[prefix] = {}
            adjacency_matrix[prefix][suffix] = 1

    ordered_adjacency_matrix = sorted(adjacency_matrix)
    adjacency_list = []
    for pattern in ordered_adjacency_matrix:
        receiver = ""
        for receivers in adjacency_matrix[pattern].keys():
            receiver += r"{},".format(receivers) * adjacency_matrix[pattern][receivers]
        receiver = r"{} -> ".format(pattern) + receiver[:-1]
        adjacency_list.append(receiver)
    return adjacency_list

with open(sys.argv[1],'r') as lh:
    i = 0
    kmers = []
    for line in lh:
        kmers.append(line[:-1])

for result in de_brujin(kmers):
    print(result)



