#! /usr/bin/python

import sys

gencode = {
    'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
    'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
    'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
    'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W'}

def rna2dna(seq):
    l_seq = len(seq)
    return ''.join(['T' if i == 'U' else i for i in seq])

amino_acid_code = {v:[] for _,v in gencode.items()}

for k,v in gencode.items():
    amino_acid_code[v].append(k)

def rna_aa(sequence):
    seq_len = len(sequence)
    aa = ""
    for i in range(0, seq_len, 3):
        #print(gencode[sequence[i:i+3]])
        if gencode.get(sequence[i:i+3]):
            aa += gencode[sequence[i:i+3]]
        else:
            break
    return aa


print(rna_aa(rna2dna(sys.argv[1])))
