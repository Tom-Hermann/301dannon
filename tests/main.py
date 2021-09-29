#!/usr/bin/python3
##
## EPITECH PROJECT, 2021
## B-MAT-500-RUN-5-1-301dannon-tom.hermann
## File description:
## tests
##

import unittest
from src.algorythm import *

class TestStringMethods(unittest.TestCase):

    def test_selection_sort(self):
        self.assertEqual(selectionSort([3.3, 5, 9.89, -6]), 6)
        self.assertEqual(selectionSort([-564, 1340, 42, 129, 858, 1491, 1508, 246, -1281, 655, 1506, 306, 290, -768, 116, 765, -48, -512, 2598, 42, 2339]), 210)
    def test_insertion_sort(self):
        self.assertEqual(insertionSort([3.3, 5, 9.89, -6]), 4)
        self.assertEqual(insertionSort([-564, 1340, 42, 129, 858, 1491, 1508, 246, -1281, 655, 1506, 306, 290, -768, 116, 765, -48, -512, 2598, 42, 2339]), 125)
    def test_bubble_sort(self):
        self.assertEqual(bubbleSort([3.3, 5, 9.89, -6]), 6)
        self.assertEqual(bubbleSort([-564, 1340, 42, 129, 858, 1491, 1508, 246, -1281, 655, 1506, 306, 290, -768, 116, 765, -48, -512, 2598, 42, 2339]), 210)
    def test_quick_sort(self):
        self.assertEqual(quickSort([3.3, 5, 9.89, -6]), 4)
        self.assertEqual(quickSort([-564, 1340, 42, 129, 858, 1491, 1508, 246, -1281, 655, 1506, 306, 290, -768, 116, 765, -48, -512, 2598, 42, 2339]), 80)
    def test_merge_sort(self):
        self.assertEqual(mergeSort([3.3, 5, 9.89, -6]), 5)
        self.assertEqual(mergeSort([-564, 1340, 42, 129, 858, 1491, 1508, 246, -1281, 655, 1506, 306, 290, -768, 116, 765, -48, -512, 2598, 42, 2339]), 67)

if __name__ == '__main__':
    unittest.main()