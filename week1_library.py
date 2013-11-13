__author__ = 'rob'

from collections import Counter


def find_kmers_with_frequency_count(sequence, length):
    counter = Counter()
    position = 0

    while position < (len(sequence) - length):
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


def mutate_kmer_at_position(kmer, position):
    real_value = kmer[position]
    end = len(kmer)
    mutations = list()
    if real_value == "A":
        mutations.append(kmer[0:position] + "C" + kmer[position+1:end])
        mutations.append(kmer[0:position] + "G" + kmer[position+1:end])
        mutations.append(kmer[0:position] + "T" + kmer[position+1:end])
    elif real_value == "C":
        mutations.append(kmer[0:position] + "A" + kmer[position+1:end])
        mutations.append(kmer[0:position] + "G" + kmer[position+1:end])
        mutations.append(kmer[0:position] + "T" + kmer[position+1:end])
    elif real_value == "G":
        mutations.append(kmer[0:position] + "A" + kmer[position+1:end])
        mutations.append(kmer[0:position] + "C" + kmer[position+1:end])
        mutations.append(kmer[0:position] + "T" + kmer[position+1:end])
    elif real_value == "T":
        mutations.append(kmer[0:position] + "A" + kmer[position+1:end])
        mutations.append(kmer[0:position] + "C" + kmer[position+1:end])
        mutations.append(kmer[0:position] + "G" + kmer[position+1:end])

    return mutations


def mutate_kmer(kmer, allowed_mismatches):
    mutations = list()
    position = 0
    while position <= len(kmer):
        # for each position do a mutation, up to 3
        # Do pos 0, then 1, then 2, then 1, 2, 3, then 0, 2, 3
        mutations.extend(mutate_kmer_at_position(kmer, position))


from itertools import product


def create_possible_kmers(k):
    possibles = list()
    charSet = 'ATCG'
    for wordchars in product(charSet, repeat=k):
        possibles.append(''.join(wordchars))

    return possibles


def find_frequent_words_with_mismatches(genome, k, allowed_mismatches):
    exacts = find_kmers_with_frequency_count(genome, k)
    possible_kmers = create_possible_kmers(k)

    exacts_to_possible_matches = dict()
    possibles_that_are_approx = list()

    # for each possible_match, call is_approx_match on it, if so, track
    for i in exacts:
        for j in possible_kmers:
            if is_approx_match(i, j, allowed_mismatches):
                #exacts_to_possible_matches[i].append(j)
                possibles_that_are_approx.append(j)



    return matches
