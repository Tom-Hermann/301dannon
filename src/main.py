#!/usr/bin/python3

from sys import argv
from src.error import error
from src.algorythm import selectionSort, insertionSort, bubbleSort, quickSort, mergeSort


def main():
    plurial = lambda x : "s" if x > 1 else ""
    list = error(argv[1:])
    print("{} element{}".format(len(list), plurial(len(list))))
    res = selectionSort(list.copy())
    print("Selection sort: {} comparison{}".format(res, plurial(res)))
    res = insertionSort(list.copy())
    print("Insertion sort: {} comparison{}".format(res, plurial(res)))
    res = bubbleSort(list.copy())
    print("Bubble sort: {} comparison{}".format(res, plurial(res)))
    res = quickSort(list.copy())
    print("Quicksort: {} comparison{}".format(res, plurial(res)))
    res = mergeSort(list.copy())
    print("Merge sort: {} comparison{}".format(res, plurial(res)))
    exit(0)

if __name__ == "__main__":
    main()
