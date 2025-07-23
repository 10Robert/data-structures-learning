from codecs import lookup


def merge_sort(unsorted_list):
    if len(unsorted_list) == 1:
        return unsorted_list
    
    mid_point = int(len(unsorted_list) / 2)
    first_half = unsorted_list[:mid_point]
    second_half = unsorted_list[mid_point:]

    half_a = merge_sort(first_half)
    half_b = merge_sort(second_half)

    return merge(half_a, half_b)

def merge(first_sublist, second_sublist):
    i = j = 0
    merged_list = []
    while i < len(first_sublist) and j < len(second_sublist):
        if first_sublist[i] < second_sublist[j]:
            merged_list.append(first_sublist[i])
            i += 1
        else:
            merged_list.append(second_sublist[j])
            j += 1
    while i < len(first_sublist):
        merged_list.append(first_sublist[i])
        i += 1
    while j < len(second_sublist):
        merged_list.append(second_sublist[j])
        j += 1
    return merged_list

lista = [11, 12, 7, 41, 61, 13, 16, 14]
print(merge_sort(lista))

""" Ordenacao por mesclagem e um algoritmo para ordenacao de uma lista de n numeros naturais na ordem crescente
"""


def reverse_merge_sort(unsorted_list):
    if len(unsorted_list) == 1:
        return unsorted_list
    
    mid_point = int(len(unsorted_list) / 2)
    first_half = unsorted_list[:mid_point]
    second_half = unsorted_list[mid_point:]

    half_a = reverse_merge_sort(first_half)
    half_b = reverse_merge_sort(second_half)

    return reverse_merge(half_a, half_b)

def reverse_merge(first_sublist, second_sublist):
    i = j = 0
    merged_list = []
    while i < len(first_sublist) and j < len(second_sublist):
        if first_sublist[i] > second_sublist[j]:
            merged_list.append(first_sublist[i])
            i += 1
        else:
            merged_list.append(second_sublist[j])
            j += 1
    while i < len(first_sublist):
        merged_list.append(first_sublist[i])
        i += 1
    while j < len(second_sublist):
        merged_list.append(second_sublist[j])
        j += 1
    return merged_list

print(reverse_merge_sort(lista))

#Calculo da serie de fibonacci

def fib(n):
    if n <= 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
    
for i in range(5):
    print(fib(i))

def dyna_fib(n):
    if n == 0:
        return 0
    if n == 1: 
        return 1
    if lookup[n] is not None:
        return lookup[n]
    
    lookup[n] = dyna_fib(n-1) + dyna_fib(n-2)
    return lookup[n]

lookup = [None] * (1000)

for i in range(6):
    print(dyna_fib(i))