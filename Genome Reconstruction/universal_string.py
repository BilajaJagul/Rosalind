#! /usr/bin/python

import sys
import itertools
import random

def kmer(k):
    if k == 1:
        return ['0','1']
    return [i[0]+i[1] for i in list(itertools.product(kmer(k-1),['0','1']))]

def adj_mat(k):
    sequences = list(set(kmer(k)))
    #print(len(sequences))
    k = len(sequences[0])
    l = len(sequences)
    adj_matrix = {}
    for sequence in sequences:
        prefix = sequence[:k-1]
        suffix = sequence[1:]
        if adj_matrix.get(prefix):
            adj_matrix[prefix]["unvisited"].append(suffix)
        else:
            adj_matrix[prefix]={}
            adj_matrix[prefix]["unvisited"] = [suffix]
            adj_matrix[prefix]["visited"] = []
    return eulerian_cycle(adj_matrix)
    
def eulerian_cycle(adj_matrix):
    #print(adj_matrix)
    starting_points = list(adj_matrix.keys())
    if len(starting_points) > 1:
        point = random.randint(0, len(starting_points)-1)
    else:
        point = 0
    start = starting_points[point]
    end = ""
    new_starts = {}
    #print(adj_matrix)
    if len(starting_points) > 1:
        point = random.randint(0, len(starting_points)-1)
    else:
        point = 0
    start = starting_points[point]
    first_start = starting_points[point]
    end = ""
    new_starts = {}
    cycle = [start]
    while first_start != end or adj_matrix[start]["unvisited"]:
        end = start
        if adj_matrix[start]["unvisited"]:
            unvisited = adj_matrix[end]["unvisited"]
            if len(unvisited) > 1:
                point = random.randint(0, len(unvisited)-1)
            else:
                point = 0
            start = adj_matrix[end]["unvisited"].pop(point)
            #print(start)
            adj_matrix[end]["visited"].append(start)
            cycle.append(start)
            if adj_matrix[end]["unvisited"]:
                new_starts[end] = 1
        end = start
    Flag = False
    #print(cycle)
    #print(adj_matrix)
    for key in adj_matrix.keys():
        if adj_matrix[key]["unvisited"]:
            Flag = True
    while Flag:
        start_positions = list(new_starts.keys())
        if len(start_positions) > 1:
            point = random.randint(0, len(start_positions)-1)
        else:
            point = 0
        start, first_start = start_positions[point], start_positions[point]
        new_cycle = [start]
        for j in range(len(cycle)):
            #print(cycle[j])
            #print(start)
            if cycle[j] == start:
                if j == 0:
                    prefix = []
                else:
                    prefix = cycle[:j]
                if j == len(cycle)-1:
                    suffix = []
                else:
                    suffix = cycle[j+1:-1]
                new_cycle += suffix
                new_cycle += prefix
                new_cycle += [start]
                break
        end = ""
        while end != first_start or adj_matrix[start]["unvisited"]:
            end = start
            if adj_matrix[start]["unvisited"]:
                unvisited = adj_matrix[end]["unvisited"]
                if len(unvisited) > 1:
                    point = random.randint(0, len(unvisited)-1)
                else:
                    point = 0
                start = adj_matrix[end]["unvisited"].pop(point)
                adj_matrix[end]["visited"].append(start)
                new_cycle.append(start)
                if adj_matrix[end]["unvisited"]:
                    new_starts[end] = 1
            end = start
        #print(newi_cycle)
        #print(adj_matrix)
        Flag = False
        for key in adj_matrix.keys():
            if adj_matrix[key]["unvisited"]:
                Flag = True
        for position in start_positions:
            new_starts[position] = 1
        cycle = new_cycle

    genome = ""
    for j in range(len(cycle)-1):
        genome += cycle[j][0]
    return genome

print(adj_mat(int(sys.argv[1])))
