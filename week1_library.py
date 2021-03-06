__author__ = 'rob'

from collections import Counter


def find_kmers_with_frequency_count(sequence, length):
    counter = Counter()
    position = 0

    while position <= (len(sequence) - length):
        nmer = sequence[position:position+length]
        counter[nmer] += 1
        position += 1

    return counter


def find_frequent_words(sequence, length):
    kmers_with_frequency = find_kmers_with_frequency_count(sequence, length)
    highest_frequency = kmers_with_frequency.most_common(1)[0][1]
    matching_kmers_sorted_by_frequency = sorted(kmers_with_frequency, key=kmers_with_frequency.get, reverse=True)

    #print("All n-mers: " + str(matching_kmers_sorted_by_frequency))
    highest_ones = []
    for kmer in matching_kmers_sorted_by_frequency:
        if kmers_with_frequency[kmer] < highest_frequency:
            break
        highest_ones.append(kmer)

    return highest_ones


def allindices(string, sub, listindex=[], offset=0):
    i = string.find(sub, offset)
    while i >= 0:
        listindex.append(i)
        i = string.find(sub, i + 1)
    return listindex


class KmerInformation:
    kmer = ""
    starting_indices = []
    count = 0
    is_already_matching = False

    def __init__(self):
        self.starting_indices = list()


def find_clumps(genome, kmer_length, window_length, minimum_frequency):
    position = 0
    kmers = dict()
    while position <= (len(genome) - kmer_length):
        current_kmer = genome[position:position+kmer_length]
        #print("Looking at " + current_kmer + " at index: " + str(position))
        match = kmers.get(current_kmer)
        if match is not None:
            # Existing match
            match_indices = match.starting_indices

            #
            # Too primitive.  What if the new one is a better index?
            #
            if position - match_indices[-1] < kmer_length:
                # In existing kmer match for this
                position += 1
                continue

            if match.is_already_matching == True:
                position += 1
                continue

            while (position + kmer_length) - match_indices[0] > window_length:
                match_indices.pop(0)
                match.count -= 1
                if match.count == 0:
                    break

            match.count += 1
            match.starting_indices.append(position)

            if match.count >= minimum_frequency:
                match.is_already_matching = True

        elif match is None:
            # new match
            info = KmerInformation()
            info.kmer = current_kmer
            info.starting_indices.append(position)
            info.count += 1
            kmers[current_kmer] = info

        position += 1

    results = list()
    for key in kmers.keys():
        if kmers[key].is_already_matching:
            results.append(key)


    return sorted(results)


def skew_prefix(genome, prefix):
    position = 0
    skew_prefix_values = []
    skew_prefix_values.append(0)
    while position < len(genome) and position < prefix:
        if genome[position] == 'C':
            skew_prefix_values.append(skew_prefix_values[position] - 1)
        elif genome[position] == 'G':
            skew_prefix_values.append(skew_prefix_values[position] + 1)
        else:
            skew_prefix_values.append(skew_prefix_values[position])
        position += 1

    return skew_prefix_values


def is_approx_match(pattern, text, allowed_mismatches):
    pos = 0
    mismatches = 0
    while pos < len(text):
        if text[pos] != pattern[pos]:
            mismatches += 1

        if mismatches > allowed_mismatches:
            break
        if pos == len(text) - 1:
            return True

        pos += 1

    return False


def find_approximate_pattern_matches(pattern, genome, allowed_mismatches):
    partial_matches = list()
    position = 0
    pattern_length = len(pattern)
    while position <= (len(genome) - pattern_length):
        kmer = genome[position:position + pattern_length]
        if is_approx_match(pattern, kmer, allowed_mismatches) is True:
            partial_matches.append(position)

        position += 1

    return partial_matches


def mutate_char(nucleotide):
    if nucleotide == "A":
        return ["C", "G", "T"]
    elif nucleotide == "C":
        return ["A", "G", "T"]
    elif nucleotide == "G":
        return ["A", "C", "T"]
    elif nucleotide == "T":
        return ["A", "C", "G"]


def recursive_mismatches(kmer, position, allowed_mismatches, mismatches):
    if position < len(kmer) and allowed_mismatches > 0:
        mutations = mutate_char(kmer[position])
        k = len(kmer)
        for m in mutations:
            mismatches.append(kmer[0:position] + m + kmer[position+1:k])
            recursive_mismatches(kmer[0:position] + m + kmer[position+1:k], position + 1, allowed_mismatches - 1, mismatches)
        recursive_mismatches(kmer, position + 1, allowed_mismatches, mismatches)
    return mismatches


def generate_mutations_for_kmer(kmer, allowed_mismatches):
    return recursive_mismatches(kmer, 0, allowed_mismatches, [])


def count_kmer_and_mismatches(allowed_mismatches, counter, highest, nmer):
    counter[nmer] += 1
    if counter[nmer] > highest:
        highest = counter[nmer]
    mismatches = generate_mutations_for_kmer(nmer, allowed_mismatches)
    for mm in mismatches:
        counter[mm] += 1
        if counter[mm] > highest:
            highest = counter[mm]
    return highest


def find_kmers_with_frequency_count_with_mismatch(genome, k, allowed_mismatches, use_reverse_complement = False):
    counter = Counter()
    highest = 0
    position = 0

    while position <= (len(genome) - k):
        nmer = genome[position:position+k]
        highest = count_kmer_and_mismatches(allowed_mismatches, counter, highest, nmer)

        if use_reverse_complement is True:
            highest = count_kmer_and_mismatches(allowed_mismatches, counter, highest, create_reverse_complement(nmer))

        position += 1

    return (highest, counter)


def find_frequent_words_with_mismatches(genome, k, allowed_mismatches):
    (highest, counter) = find_kmers_with_frequency_count_with_mismatch(genome, k, allowed_mismatches)
    return_list = []
    for kmer in counter.keys():
        if counter[kmer] == highest:
            return_list.append(kmer)

    return sorted(return_list)


def find_frequent_words_with_mismatches_and_reverse_complements(genome, k, allowed_mismatches):
    (highest, counter) = find_kmers_with_frequency_count_with_mismatch(genome, k, allowed_mismatches, True)
    return_list = []
    for kmer in counter.keys():
        if counter[kmer] == highest:
            return_list.append(kmer)

    return sorted(return_list)


def create_reverse_complement(genome):
    complements = {'A': 'T', 'C': 'G', 'T': 'A', 'G': 'C'}

    nucleotides = list(genome)
    reverseComplement = ""
    for nucl in nucleotides:
        reverseComplement += complements[nucl]
    return reverseComplement[::-1]