##
## EPITECH PROJECT, 2021
## B-MAT-500_301dannon
## File description:
## algorythm
##

def selectionSort(array):
    comp = 0

    for i in range(len(array)):
        min  =  i
        for j in range(i + 1, len(array)):
            comp += 1
            if (array[j] < array[min]):
                min = j
            array[i], array[min] = array[min], array[i]
    return comp


def insertionSort(array):
    length = len(array)
    comp = 0

    for i in range(1, length):
        while i > 0:
            comp += 1
            if array[i - 1] <= array[i]:
                array[i], array[i - 1] = array[i - 1], array[i]
                i -= 1
            else:
                break
    return comp


def bubbleSort(array):

    comp = 0
    n = len(array)

    for i in range(n):
        for j in range(0, n-i-1):
            comp += 1
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return comp



def quickSort(org):

    if len(org) == 0 or len(org) == 1:
        return 0

    itteration, pivot = 0, 0
    left, right = [], []

    for i in range(len(org)):
        if i != pivot:
            itteration += 1
            if (org[i] < org[pivot]):
                left.append(org[i])
            else:
                right.append(org[i])
    return itteration + quickSort(right) + quickSort(left)


def mergeSort(array):

    comp = 0

    mid = len(array) // 2
    left = array[:mid]
    right = array[mid:]

    if (len(left) > 1):
        comp += mergeSort(left)

    if (len(right) > 1):
        comp += mergeSort(right)

    i = 0
    j = 0
    k = 0

    while i < len(left) and j < len(right):
        comp += 1
        if left[i] <= right[j]:
            array[k] = left[i]
            i += 1
        else:
            array[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        array[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        array[k] = right[j]
        j += 1
        k += 1

    return comp
