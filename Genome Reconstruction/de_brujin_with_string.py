#! /usr/bin/python

import sys

def de_brujin_string(k_og, DNA):
    k = k_og - 1
    l_seq = len(DNA)
    adjacency_matrix = {}
    for j in range(l_seq - k):
        master_kmer = DNA[j:j+k]
        new_kmer = DNA[j+1:j+k+1]
        if adjacency_matrix.get(master_kmer):
            if adjacency_matrix[master_kmer].get(new_kmer):
                adjacency_matrix[master_kmer][new_kmer] += 1
            else:
                adjacency_matrix[master_kmer][new_kmer] = 1
        else:
            adjacency_matrix[master_kmer]={}
            adjacency_matrix[master_kmer][new_kmer] = 1
    ordered_adjacency_matrix = sorted(adjacency_matrix)
    adjacency_list = []
    for pattern in ordered_adjacency_matrix:
        receiver = ""
        for receivers in adjacency_matrix[pattern].keys():
            receiver += r"{},".format(receivers)*adjacency_matrix[pattern][receivers]
        receiver = r"{} -> ".format(pattern) + receiver[:-1]
        adjacency_list.append(receiver)
    return adjacency_list

with open(sys.argv[1],'r') as lh:
    i = 0
    DNA = ""
    for line in lh:
        i = i + 1
        if i == 1:
            k = int(line[:-1])
        else:
            DNA += line[:-1]

for result in de_brujin_string(k, DNA):
    print(result)



