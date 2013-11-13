__author__ = 'rob'

import unittest
from itertools import product

from week1_library import find_frequent_words_with_mismatches

class TestSequenceFunctions(unittest.TestCase):

    def test_sample_1(self):
        find_frequent_words_with_mismatches("ACGTTGCATGTCGCATGATGCATGAGAGCT", 4, 1)



