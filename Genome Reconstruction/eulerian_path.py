#! /usr/bin/python

import sys
import random
import copy

def cycle(ad_list):
    #print(ad_list)
    ad_matrix = {}
    odd_even = {}
    dup_ad_matrix = {}
    unbalanced_vertex_incoming = []
    unbalanced_vertex_outgoing = []
    for item in ad_list:
        subitems = item.split('->')
        if ad_matrix.get(subitems[0][:-1]):
            receiver_list = subitems[1][1:]
            receivers = receiver_list.split(',')
            ad_matrix[subitems[0][:-1]]["unvisited"] += receivers
        else:
            receivers = subitems[1][1:].split(',')
            ad_matrix[subitems[0][:-1]] = {}
            ad_matrix[subitems[0][:-1]]["unvisited"] = []
            ad_matrix[subitems[0][:-1]]["unvisited"] += receivers
            ad_matrix[subitems[0][:-1]]["visited"] = []
        if odd_even.get(subitems[0][:-1]):
            odd_even[subitems[0][:-1]] += 1 * len(receivers)
        else:
            odd_even[subitems[0][:-1]] = 1 * len(receivers)
        for receiver in receivers:
            if odd_even.get(receiver):
                odd_even[receiver] -= 1
            else:
                odd_even[receiver] = -1
    for key in odd_even.keys():
        if odd_even[key] > 0:
            unbalanced_vertex_outgoing.append(key)
        elif odd_even[key] < 0:
            unbalanced_vertex_incoming.append(key)
    
    start = unbalanced_vertex_outgoing[0]
    new_starts = {}
    end = ""
    cycle = [start]
    while ad_matrix.get(start) and ad_matrix[start]["unvisited"]:
        end = start
        if len(ad_matrix[start]["unvisited"]) == 1:
            point = 0
        else:
            point = random.randint(0, len(ad_matrix[start]["unvisited"])-1)
        start = ad_matrix[end]["unvisited"].pop(point)
        ad_matrix[end]["visited"].append(start)
        cycle.append(start)
        if ad_matrix[end]["visited"]:
            new_starts[end] = 1
        end =start
    Flag = False
    for key in ad_matrix.keys():
        if ad_matrix[key]["unvisited"]:
            Flag = True

    while Flag:
        start_positions = list(new_starts.keys())
        if len(start_positions) <= 1:
            point = 0
        else:
            point = random.randint(0, len(start_positions)-1)
        new_start = start_positions[point]
        new_starts = {}
        end = ""
        for j in range(len(cycle)):
            if cycle[j] == new_start:
                if j == 0:
                    prefix = []
                else:
                    prefix = cycle[:j]
                if j == len(cycle)-1:
                    suffix = []
                else:
                    suffix = cycle[j+1:]
                #print(cycle)
                #print(suffix)
                break
        cycle = [new_start]
        while ad_matrix.get(new_start) and ad_matrix[new_start]["unvisited"]:
            end = new_start
            if len(ad_matrix[new_start]["unvisited"]) == 1:
                point = 0
            else:
                point = random.randint(0, len(ad_matrix[new_start]["unvisited"])-1)
            new_start = ad_matrix[end]["unvisited"].pop(point)
            ad_matrix[end]["visited"].append(new_start)
            cycle.append(new_start)
            if ad_matrix[end]["visited"]:
                new_starts[end] = 1
            end = new_start
        
        Flag = False
        for key in ad_matrix.keys():
            if ad_matrix[key]["unvisited"]:
                Flag = True
        for start in start_positions:
            new_starts[start]=1

        cycle = prefix + cycle + suffix

    return cycle
with open(sys.argv[1],'r') as lh:
    i = 0
    ad_list = []
    for line in lh:
        ad_list.append(line[:-1])

result = cycle(ad_list)
r1 = result[0]
for r in range(1, len(result)):
    if result[r] != result[r-1]:
        r1 += r"->{}".format(result[r])

print(r1)


