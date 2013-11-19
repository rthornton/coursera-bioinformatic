__author__ = 'rob'

import unittest
from week2.week2_library import find_nmers_for_peptide, walk_reading_frame_for_sequences, convert_peptide_to_possible_sequences

class TestSequenceFunctions(unittest.TestCase):

    def test_sample_1(self):
        genome = "ATGGCCATGGCCCCCAGAACTGAGATCAATAGTACCCGTATTAACGGGTGA"
        peptide = "MA"
        self.assertEqual(['ATGGCC', 'GGCCAT', 'ATGGCC'], find_nmers_for_peptide(genome, peptide))


    def walk_reading_frame_for_sequences(self):
        frame = ""
        peptide = "MA"
        possible_sequences = convert_peptide_to_possible_sequences(peptide)
        self.assertEqual()
