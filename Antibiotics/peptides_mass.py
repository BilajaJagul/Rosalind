#! /usr/bin/python

import os, sys

weights = []

with open(sys.argv[1],'r') as lh:
    amino_acid_weights = {}
    for line in lh:
        if line[-1] == "\n":
            data = line[:-1].split(" ")
        else:
            data = line.split(" ")
        #print(data)
        amino_acid_weights[data[0]] = int(data[1])
        weights.append(int(data[1]))
    weights = sorted(list(set(weights)))

def mass_pept(mass):
    #print(weights)
    value = [0 for j in range(mass + 1)]
    for j in range(1, mass+1):
        for i in range(len(weights)):
            if int(weights[i]) < j:
                value[j] += value[j-int(weights[i])]
            elif int(weights[i]) == j:
                value[j] += 1
    return value[mass]

print(mass_pept(int(sys.argv[2])))

