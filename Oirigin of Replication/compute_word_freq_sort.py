#! /bin/usr/python

import sys
import random

def pattern_to_number(pattern):
    mapping = {'A':0,'C':1,'G':2,'T':3}
    if not pattern:
        return 0
    return 4 * pattern_to_number(pattern[:-1]) + mapping[pattern[-1]]

def number_to_pattern(number, k):
    mapping = ['A','C','G','T']
    if k == 1:
        return mapping[number]
    return "" + number_to_pattern(number//4, k-1) + mapping[number % 4]

def most_freq(array):
    local_count = 1
    max_count = 0
    max_element = [array[0]]
    local_element = array[0]
    for j in range(1, len(array)):
        if local_element == array[j]:
            local_count += 1
        else:
            if local_count > max_count:
                max_count = local_count
                max_element = [local_element]
            elif local_count == max_count:
                max_element.append(local_element)
            local_count = 1
            local_element = array[j]
    return(max_element)

def partition(A, l, r):
    i = l
    for j in range(l, r):
        if A[j] < A[l]:
            i = i + 1
            A[i], A[j] = A[j], A[i]
    A[i], A[l] = A[l], A[i]
    return i

def quick_sort(A, l, r):
    if l >= r:
        return
    k = random.randint(l, r-1)
    A[k],A[l] = A[l], A[k]
    m = partition(A, l, r)
    quick_sort(A, l, m)
    quick_sort(A, m+1, r)
    return A


def sort_freq_counter(sequence, k):
    l_seq = len(sequence)
    freq_arr = []
    for j in range(0, l_seq - k + 1):
        pattern = pattern_to_number(sequence[j:j+k])
        freq_arr.append(pattern)
    freq_arr = quick_sort(freq_arr, 0, len(freq_arr))
    sequence = []
    max_freq = most_freq(freq_arr)
    for j in max_freq:
        sequence.append(number_to_pattern(j,k))
    return sequence

#arr = sys.argv[1].split(',')
#arr = [int(i) for i in arr]
#print(quick_sort(arr,0,len(arr)))

print(sort_freq_counter(sys.argv[1], int(sys.argv[2])))
