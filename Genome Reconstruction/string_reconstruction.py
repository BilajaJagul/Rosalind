#! /usr/bin/python

import sys
import random

def adjacency_matrix(sequences):
    k = len(sequences[0])
    l = len(sequences)
    adj_matrix = {}
    odd_even = {}
    for sequence in range(l):
        prefix = sequences[sequence][:k-1]
        suffix = sequences[sequence][1:]
        if odd_even.get(prefix):
            odd_even[prefix] += 1
        else:
            odd_even[prefix] = 1
        if odd_even.get(suffix):
            odd_even[suffix] -= 1
        else:
            odd_even[suffix] = -1
        if adj_matrix.get(prefix):
            adj_matrix[prefix]["unvisited"].append(suffix)
        else:
            adj_matrix[prefix] = {}
            adj_matrix[prefix]["unvisited"] = [suffix]
            adj_matrix[prefix]["visited"] = []
    unbalanced_vertex_outgoing = ""
    unbalanced_vertex_incoming = ""
    for key in odd_even.keys():
        if odd_even[key] > 0:
            unbalanced_vertex_outgoing = key
        elif odd_even[key] < 0:
            unbalanced_vertex_incoming = key
    #print(adj_matrix)
    return eulerian_path(adj_matrix, unbalanced_vertex_outgoing, unbalanced_vertex_incoming)

def eulerian_path(adj_matrix, start, end):
    cycle = [start]
    new_starts = {}
    end_temp = ""
    temp_start = start
    while adj_matrix.get(temp_start) and adj_matrix[temp_start].get("unvisited"):
        end_temp = temp_start
        unvisited = adj_matrix[temp_start]["unvisited"]
        if len(unvisited) == 1:
            point = 0
        else:
            point = random.randint(0, len(unvisited)-1)
        temp_start = adj_matrix[end_temp]["unvisited"].pop(point)
        adj_matrix[end_temp]["visited"].append(temp_start)
        cycle.append(temp_start)
        if adj_matrix[end_temp]["unvisited"]:
            new_starts[end] = 1
        temp_end = temp_start

    Flag = False
    for key in adj_matrix.keys():
        if adj_matrix[key]["unvisited"]:
            Flag = True

    while Flag:
        start_positions = list(new_starts.keys())
        if len(start_positions) == 1:
            point = 0
        else:
            point = random.randint(0, len(start_positions)-1)
        temp_start = start_positions[point]
        new_starts = {}
        temp_end = ""
        for j in range(len(cycle)):
            if cycle[j] == temp_start:
                if j == 0:
                    prefix = []
                else:
                    prefix = cycle[:j]
                if j == len(cycle):
                    suffix = []
                else:
                    suffix = cycle[j+1:]
                break
        cycle = [temp_start]

        while adj_matrix[temp_start] and adj_matrix[temp_start]["unvisited"]:
            temp_end = temp_start
            unvisited = adj_matrix[temp_start]["unvisited"]
            if len(unvisited) == 1:
                point = 0
            else:
                point = random.randint(0, len(unvisited)-1)
            temp_start = adj_matrix[temp_start]["unvisited"].pop(point)
            adj_matrix[temp_end]["visited"].append(temp_start)
            if adj_matrix[temp_end]["unvisited"]:
                new_starts[temp_end] = 1
            temp_end = temp_start

        Flag = False
        for key in ad_matrix.keys():
            if ad_matrix[key]["unvisited"]:
                Flag = True
        for start in start_positions:
            new_starts[start] = 1

        cycle = prefix + cycle + suffix

    genome = ""
    for kmer in range(len(cycle)-1):
        genome += cycle[kmer][0]
    genome += cycle[-1]

    return genome


with open(sys.argv[1],'r') as lh:
    i = 0
    sequences = []
    for line in lh:
        i = i + 1
        if i > 1:
            sequences.append(line[:-1])

print(adjacency_matrix(sequences))


