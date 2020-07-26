import sys

with open(sys.argv[1],'r') as lh:
    amino_acid_weights = {}
    for line in lh:
        data = line[:-1].split(" ")
        amino_acid_weights[data[0]] = data[1]


def cyclic_spectrum(peptide):
    l_peptide = len(peptide)
    prefix_mass = [0]
    for j in range(len(peptide)):
        prefix_mass += [prefix_mass[-1] + int(amino_acid_weights[peptide[j]])]
    
    #print(prefix_mass)

    full_mass = prefix_mass[l_peptide]

    cyclic_spectrum = [0]

    for j in range(0, l_peptide):
        for i in range(j+1,l_peptide + 1):
            cyclic_spectrum.append(prefix_mass[i] -  prefix_mass[j])
            if j > 0 and i < l_peptide:
                cyclic_spectrum.append(full_mass - (prefix_mass[i] - prefix_mass[j]))
    return sorted(cyclic_spectrum)

result = cyclic_spectrum(sys.argv[2])

for res in result:
    print(res, end = " ")
