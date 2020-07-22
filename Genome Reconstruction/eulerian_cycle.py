#! /usr/bin/python

import sys
import random
import copy

def cycle(ad_list):
    ad_matrix = {}
    dup_ad_matrix = {}
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
    dup_ad_matrix = copy.deepcopy(ad_matrix)
    start_positions = list(ad_matrix.keys())
    start_position = random.randint(0, len(start_positions)-1)
    new_starts = {}
    end = ""
    start, first_start = start_positions[start_position],start_positions[start_position]
    cycle = [start]
    while end != first_start or len(ad_matrix[start]["unvisited"]) > 0:
        end = start
        spot = random.randint(0, len(ad_matrix[end]["unvisited"])-1)
        start = ad_matrix[end]["unvisited"].pop(spot)
        ad_matrix[end]["visited"].append(start)
        cycle.append(start)
        if ad_matrix[end]["unvisited"]:
            new_starts[end] = 1
        end = start
    Flag = False
    for key in ad_matrix.keys():
        if ad_matrix[key]["unvisited"]:
            Flag = True
    while Flag:
        start_positions = list(new_starts.keys())
        start_position = random.randint(0, len(start_positions)-1)
        new_starts = {}
        end = ""
        start, first_start = start_positions[start_position],start_positions[start_position]
        new_cycle = [start]
        for j in range(len(cycle)):
            if cycle[j] == start:
                if j == 0:
                    prefix = []
                else:
                    prefix = cycle[:j+1]
                if j == len(cycle)-1:
                    suffix = []
                else:
                    suffix = cycle[j+1:-1]
                new_cycle += suffix
                new_cycle += prefix
                break
        while end != first_start or len(ad_matrix[start]["unvisited"]) > 0:
            end = start
            if ad_matrix[end]["unvisited"]:
                spot = random.randint(0, len(ad_matrix[start]["unvisited"])-1)
                start = ad_matrix[end]["unvisited"].pop(spot)
                ad_matrix[end]["visited"].append(start)
            new_cycle.append(start)
            if ad_matrix[end]["unvisited"]:
                new_starts[end] = 1
            end = start
        Flag = False
        for key in ad_matrix.keys():
            if ad_matrix[key]["unvisited"]:
                Flag = True
        for position in start_positions:
            new_starts[position] = 1
        cycle = new_cycle
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


