__author__ = 'rob'

import unittest
from itertools import product

from week1_library import find_frequent_words_with_mismatches, generate_mutations_for_kmer, find_frequent_words_with_mismatches_and_reverse_complements

class TestSequenceFunctions(unittest.TestCase):

    def test_generate_mutations_simple(self):
        mismatches = generate_mutations_for_kmer("A", 1)
        self.assertEqual(["C", "G", "T"], mismatches)

        mismatches = generate_mutations_for_kmer("AC", 1)
        self.assertEqual(["AA", "AG", "AT", "CC", "GC", "TC"], sorted(mismatches))


    def test_generate_mutations(self):
        mismatches = generate_mutations_for_kmer("ACG", 2)
        print(sorted(mismatches))
        #self.assertEqual(["AAA", "AAG", "ACC", "ACT", "CCG", "GC", "TC"], sorted(mismatches))
        expected_values = ["AAA", "AAG", "ACC", "ACT", "CCG", "GCG", "GGG", "TCT"]
        for ev in expected_values:
            self.assertTrue(ev in mismatches, ev)

        for mm in mismatches:
            self.assertEqual(3, len(mm))


    def test_sample_1(self):
        matches = find_frequent_words_with_mismatches("ACGTTGCATGTCGCATGATGCATGAGAGCT", 4, 1)
        self.assertEqual("ATGC ATGT GATG", " ".join(matches))


    def test_extra_dataset(self):
        matches = find_frequent_words_with_mismatches("CACAGTAGGCGCCGGCACACACAGCCCCGGGCCCCGGGCCGCCCCGGGCCGGCGGCCGCCGGCGCCGGCACACCGGCACAGCCGTACCGGCACAGTAGTACCGGCCGGCCGGCACACCGGCACACCGGGTACACACCGGGGCGCACACACAGGCGGGCGCCGGGCCCCGGGCCGTACCGGGCCGCCGGCGGCCCACAGGCGCCGGCACAGTACCGGCACACACAGTAGCCCACACACAGGCGGGCGGTAGCCGGCGCACACACACACAGTAGGCGCACAGCCGCCCACACACACCGGCCGGCCGGCACAGGCGGGCGGGCGCACACACACCGGCACAGTAGTAGGCGGCCGGCGCACAGCC", 10, 2)
        self.assertEqual("GCACACAGAC GCGCACACAC", " ".join(matches))


    def test_submittal(self):
        matches = find_frequent_words_with_mismatches("TAACTAGTAGCCCAGTAGCGCCCACCCATAACTAGTAGTAACTAGAGCGTAGAGCGAGCGGTGTCCCAAGCGAGCGTAACAGCGGTCCCACCCAAGCGAGCGCCCACCCACCCAGTCCCAGTTAACCCCAGTAGCGGTTAGTAACCCCAAGCGGTAGCGTAGCCCAAGCGAGCGAGCGGTAGCGCCCATAACTAACGTCCCACCCAAGCGAGCGAGCGGTAGCGGTAGCGTAGTAGGTAGCGCCCAGTAGCGCCCAGTCCCACCCATAACAGCGTAACTAACGTAGCGTAGGTGTTAACCCCAGTAGCGTAACTAGTAACGTTAACCCCACCCAAGCGCCCAGTTAACGTAGCGAGCGAGCGAGCGTAGCCCATAAC", 8, 2)
        self.assertEqual("CGCTAGCG", " ".join(matches))


    def test_sample_1_reverse_complement(self):
        matches = find_frequent_words_with_mismatches_and_reverse_complements("ACGTTGCATGTCGCATGATGCATGAGAGCT", 4, 1)
        self.assertEqual("ACAT ATGT", " ".join(matches))


    def test_extra_dataset_reverse_complement(self):
        matches = find_frequent_words_with_mismatches_and_reverse_complements("CTTGCCGGCGCCGATTATACGATCGCGGCCGCTTGCCTTCTTTATAATGCATCGGCGCCGCGATCTTGCTATATACGTACGCTTCGCTTGCATCTTGCGCGCATTACGTACTTATCGATTACTTATCTTCGATGCCGGCCGGCATATGCCGCTTTAGCATCGATCGATCGTACTTTACGCGTATAGCCGCTTCGCTTGCCGTACGCGATGCTAGCATATGCTAGCGCTAATTACTTAT", 9, 3)
        self.assertEqual("AGCGCCGCT AGCGGCGCT", " ".join(matches))


    def test_submittal_reverse_complement(self):
        matches = find_frequent_words_with_mismatches_and_reverse_complements("CTGCTGCTGTCCTACTACCCGCCGTCTACTCCTGTCCTGCCGCCTCTCCCGTCCTGCCTGCTGCCGTACCTGTACTACCCCGTACTACTACCTACTCTCTACCCGCCGCCGCCCGCCGTCTACCTGTCTACCTCCCTGTACCTACTCTACTACCCGTCTACTACTACTCCTCTACCCCGTCCTGTCCTGTACCTACCCCTGCCTGCTCCCGCCCG", 8, 3)
        self.assertEqual("CCCCCCCC GGGGGGGG", " ".join(matches))


