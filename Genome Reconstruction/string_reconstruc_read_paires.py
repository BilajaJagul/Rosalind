#! /usr/bin/python

import sys
import random

def de_brujin(sequences,k,d):
    l = len(sequences)
    adj_matrix = {}
    incoming_degree = {}
    odd_even = {}
    for j in range(l):
        prefix = sequences[j][0:k-1] + sequences[j][k+1:-1]
        suffix = sequences[j][1:k] + sequences[j][k+2:]
        if prefix and adj_matrix.get(prefix):
            adj_matrix[prefix]["unvisited"].append(suffix)
        elif prefix:
            adj_matrix[prefix]={}
            adj_matrix[prefix]["unvisited"] = [suffix]
            adj_matrix[prefix]["visited"] = []
        if suffix and not adj_matrix.get(suffix):
            adj_matrix[suffix] = {}
            adj_matrix[suffix]["unvisited"] = []
            adj_matrix[suffix]["visited"] = []
        if incoming_degree.get(suffix):
            incoming_degree[suffix] += 1
        else:
            incoming_degree[suffix] = 1
        if odd_even.get(prefix):
            odd_even[prefix] += 1
        else:
            odd_even[prefix] = 1
        if odd_even.get(suffix):
            odd_even[suffix] -= 1
        else:
            odd_even[suffix] = -1

    more_incoming = []
    more_outgoing = []
    for key in odd_even.keys():
        if odd_even[key] > 0:
            more_outgoing.append(key)
        elif odd_even[key] < 0:
            more_incoming.append(key)
    incoming_degree_greater_1 = []
    for node in incoming_degree.keys():
        if incoming_degree[node] > 1:
            incoming_degree_greater_1.append(node)
    #print(more_incoming)
    #print(more_outgoing)
    sequence_strings = eulerian_path(adj_matrix, more_outgoing[0], more_incoming[0])
    return spell(sequence_strings, k, d)
    

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
    print(cycle)
    print(adj_matrix)

    Flag = False
    for key in adj_matrix.keys():
        if adj_matrix[key]["unvisited"]:
            Flag = True

    while Flag:
        #print(start_positions)
        start_positions = list(new_starts.keys())
        print(start_positions)
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

    return cycle

def spell(sequence, k,d):
    prefixes = []
    suffixes = []
    for j in range(len(sequence)):
        prefixes.append(sequence[j][0:k-1])
        suffixes.append(sequence[j][k-1:])
    prefix_string = ""
    suffix_string = ""
    for j in range(len(prefixes)-1):
        prefix_string += prefixes[j][0]
        suffix_string += suffixes[j][0]
    prefix_string += prefixes[-1]
    suffix_string += suffixes[-1]
    print(len(prefix_string[k+d:]))
    print(len(suffix_string[:len(suffix_string) - k - d]))
    if prefix_string[k+d:] == suffix_string[:len(suffix_string) - k - d]:
        return prefix_string + suffix_string[len(suffix_string) - k - d:]
    return "Cannot Join"

with open(sys.argv[1],'r') as lh:
    i = 0
    sequences = []
    for line in lh:
        i = i + 1
        if i == 1:
            t = line[:-1].split(" ")
            k = int(t[0])
            d = int(t[1])
        else:
            sequences.append(line[:-1])



print(de_brujin(sequences, k, d))


