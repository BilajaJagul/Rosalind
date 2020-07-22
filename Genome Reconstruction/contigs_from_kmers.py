#! /usr/bin/python

import sys,os
import random

def de_brujin(kmers):
    l_kmers = len(kmers)
    k = len(kmers[0])
    adj_matrix = {}
    in_degree = {}
    out_degree = {}
    more_outgoing = []
    isolated_cycles = []
    for j in range(l_kmers):
        prefix = kmers[j][:k-1]
        suffix = kmers[j][1:]
        if adj_matrix.get(prefix):
            adj_matrix[prefix]["unvisited"].append(suffix)
        else:
            adj_matrix[prefix] = {}
            adj_matrix[prefix]["unvisited"] = [suffix]
            adj_matrix[prefix]["visited"] = []
        if out_degree.get(prefix):
            out_degree[prefix] += 1
        else:
            out_degree[prefix] = 1
        if in_degree.get(suffix):
            in_degree[suffix] += 1
        else:
            in_degree[suffix] = 1
    
    for node in out_degree.keys():
        if out_degree[node] > 1:
            more_outgoing.append(node)
        elif not in_degree.get(node):
            isolated_cycles.append(node)
    for node in in_degree.keys():
        if in_degree[node] > 1:
            more_outgoing.append(node)
    cycle = []

    for node in more_outgoing:
        start = node
        while adj_matrix.get(node) and adj_matrix[node].get("unvisited"):
            paths = [node]
            next_length = len(adj_matrix[node].get("unvisited"))
            if next_length == 1:
                next_node = adj_matrix[node]["unvisited"].pop(0)
                adj_matrix[node]["visited"].append(next_node)
            else:
                random_pos = random.randint(0,next_length - 1)
                next_node = adj_matrix[node]["unvisited"].pop(random_pos)
                adj_matrix[node]["visited"].append(next_node)
            while in_degree.get(next_node) and out_degree.get(next_node) and in_degree[next_node] == 1 and out_degree[next_node] == 1:
                paths.append(next_node)
                new_node = adj_matrix[next_node]["unvisited"].pop(0)
                adj_matrix[next_node]["visited"].append(new_node)
                next_node = new_node
            paths.append(next_node)
            cycle.append(paths)

    for node in isolated_cycles:
        start = node
        #print(node)
        paths = [node]
        next_node = adj_matrix[node]["unvisited"].pop()
        adj_matrix[node]["visited"].append(next_node)
        while in_degree.get(next_node) and out_degree.get(next_node) and in_degree[next_node] == 1 and out_degree[next_node] == 1:
            paths.append(next_node)
            new_node = adj_matrix[next_node]["unvisited"].pop(0)
            adj_matrix[next_node]["visited"].append(new_node)
            next_node = new_node
        paths.append(next_node)
        cycle.append(paths)

    contigs = []

    for contig in cycle:
        expression = contig[0]
        for letter in range(1, len(contig)):
            expression += contig[letter][-1]
        contigs.append(expression)

    return contigs


with open(sys.argv[1],'r') as lh:
    kmers = []
    for line in lh:
        kmers.append(line[:-1])

result = de_brujin(kmers)
for r in result:
    print(r, end = " ")




