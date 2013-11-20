__author__ = 'rob'

codon_to_aa = {
    'AAA': 'K',
    'AAC': 'N',
    'AAG': 'K',
    'AAU': 'N',
    'ACA': 'T',
    'ACC': 'T',
    'ACG': 'T',
    'ACU': 'T',
    'AGA': 'R',
    'AGC': 'S',
    'AGG': 'R',
    'AGU': 'S',
    'AUA': 'I',
    'AUC': 'I',
    'AUG': 'M',
    'AUU': 'I',
    'CAA': 'Q',
    'CAC': 'H',
    'CAG': 'Q',
    'CAU': 'H',
    'CCA': 'P',
    'CCC': 'P',
    'CCG': 'P',
    'CCU': 'P',
    'CGA': 'R',
    'CGC': 'R',
    'CGG': 'R',
    'CGU': 'R',
    'CUA': 'L',
    'CUC': 'L',
    'CUG': 'L',
    'CUU': 'L',
    'GAA': 'E',
    'GAC': 'D',
    'GAG': 'E',
    'GAU': 'D',
    'GCA': 'A',
    'GCC': 'A',
    'GCG': 'A',
    'GCU': 'A',
    'GGA': 'G',
    'GGC': 'G',
    'GGG': 'G',
    'GGU': 'G',
    'GUA': 'V',
    'GUC': 'V',
    'GUG': 'V',
    'GUU': 'V',
    'UAA': False,
    'UAC': 'Y',
    'UAG': False,
    'UAU': 'Y',
    'UCA': 'S',
    'UCC': 'S',
    'UCG': 'S',
    'UCU': 'S',
    'UGA': False,
    'UGC': 'C',
    'UGG': 'W',
    'UGU': 'C',
    'UUA': 'L',
    'UUC': 'F',
    'UUG': 'L',
    'UUU': 'F'
}

aa_to_rna = {
    'A': ['GCU', 'GCC', 'GCA', 'GCG'],
    'L': ['UUA', 'UUG', 'CUU', 'CUC', 'CUA', 'CUG'],
    'R': ['CGU', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'],
    'K': ['AAA', 'AAG'],
    'N': ['AAU', 'AAC'],
    'M': ['AUG'],
    'D': ['GAU', 'GAC'],
    'F': ['UUU', 'UUC'],
    'C': ['UGU', 'UGC'],
    'P': ['CCU', 'CCC', 'CCA', 'CCG'],
    'Q': ['CAA', 'CAG'],
    'S': ['UCU', 'UCC', 'UCA', 'UCG', 'AGU', 'AGC'],
    'E': ['GAA', 'GAG'],
    'T': ['ACU', 'ACC', 'ACA', 'ACG'],
    'G': ['GGU', 'GGC', 'GGA', 'GGG'],
    'W': ['UGG'],
    'H': ['CAU', 'CAC'],
    'Y': ['UAU', 'UAC'],
    'I': ['AUU', 'AUC', 'AUA'],
    'V': ['GUU', 'GUC', 'GUA', 'GUG']

#Start 	AUG 	Stop 	UAG, UGA, UAA
}


def translate_protein_from_rna(rna):
    position = 0
    peptide = ""

    while position <= (len(rna) - 3):
        codon = rna[position:position+3]
        amino_acid = codon_to_aa.get(codon)
        if not amino_acid:
            return peptide
        else:
            peptide += amino_acid

        position += 3

    return peptide


def walk_reading_frame_for_sequences(reading_frame, sequences):
    return []


def convert_peptide_to_possible_sequences_r(sequences, peptide, position):
    if position < len(peptide):
        rnas = aa_to_rna.get(peptide[position])
        position += 1
        sequences *= len(rnas)
        rna_index = 0
        while rna_index < len(rnas):
            sequences[rna_index] += rnas[rna_index]
            rna_index += 1
            #while sequence_index < len(sequences):
            ##for sequence in sequences:
            #    sequences[sequence_index] += rna
            #    convert_peptide_to_possible_sequences_r(sequences, peptide, position)
            #    sequence_index += 1

    return sequences


def convert_peptide_to_possible_sequences(peptide):
    # Backwards to RNA, then convert U to T
    sequences = []
    position = 0
    rnas = aa_to_rna.get(peptide[position])
    for rna in rnas:
        sequences.append(rna)
        convert_peptide_to_possible_sequences_r(sequences, peptide, 1)

    return sequences


class Node:
    children = []


def build_tree(peptide):
    position = 0
    head = Node()
    current_node = head
    while position < len(peptide):
        current_node.children = aa_to_rna.get(peptide[position])



def recursive_dfs(graph, start, path=[]):
    '''recursive depth first search from start'''
    path = path + [start]
    for node in graph[start]:
        if not node in path:
            path = recursive_dfs(graph, node, path)
    return path


def find_nmers_for_peptide(genome, peptide):
    # Create reading frames
        # 3 forward, 3 backward
    # Call for each
    # Append results
    return []