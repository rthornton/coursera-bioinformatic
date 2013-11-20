__author__ = 'rob'

import unittest
from week2.week2_library import find_nmers_for_peptide, walk_reading_frame_for_sequences, convert_peptide_to_possible_sequences

class TestSequenceFunctions(unittest.TestCase):

    #def test_sample_1(self):
    #    genome = "ATGGCCATGGCCCCCAGAACTGAGATCAATAGTACCCGTATTAACGGGTGA"
    #    peptide = "MA"
    #    self.assertEqual(['ATGGCC', 'GGCCAT', 'ATGGCC'], find_nmers_for_peptide(genome, peptide))


    def test_walk_reading_frame_for_sequences_simple(self):
        peptide = "MA"
        # M - AUG
        # A - 'A': ['GCU, GCC, GCA, GCG'],
        possible_sequences = convert_peptide_to_possible_sequences(peptide)
        self.assertEqual(['AUGGCU', 'AUGGCC', 'AUGGCA', 'AUGGCG'], possible_sequences)


    def test_walk_reading_frame_for_sequences_simple2(self):
        peptide = "AM"
        # M - AUG
        # A - 'A': ['GCU, GCC, GCA, GCG'],
        possible_sequences = convert_peptide_to_possible_sequences(peptide)
        self.assertEqual(['GCUAUG', 'GCCAUG', 'GCAAUG', 'GCGAUG'], possible_sequences)


