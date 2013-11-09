__author__ = 'rob'

#Frequent Words Problem: Find the most frequent k-mers in a string.
#     Input: A string Text and an integer k.
#     Output: All most frequent k-mers in Text.
#Sample Input:
#     ACGTTGCATGTCGCATGATGCATGAGAGCT
#     4
#
#Sample Output:
#     CATG GCAT

from collections import Counter

text = "ACGTTGCATGTCGCATGATGCATGAGAGCT"
text2 = "CGGAAGCGAGATTCGCGTGGCGTGATTCCGGCGGGCGTGGAGAAGCGAGATTCATTCAAGCCGGGAGGCGTGGCGTGGCGTGGCGTGCGGATTCAAGCCGGCGGGCGTGATTCGAGCGGCGGATTCGAGATTCCGGGCGTGCGGGCGTGAAGCGCGTGGAGGAGGCGTGGCGTGCGGGAGGAGAAGCGAGAAGCCGGATTCAAGCAAGCATTCCGGCGGGAGATTCGCGTGGAGGCGTGGAGGCGTGGAGGCGTGCGGCGGGAGATTCAAGCCGGATTCGCGTGGAGAAGCGAGAAGCGCGTGCGGAAGCGAGGAGGAGAAGCATTCGCGTGATTCCGGGAGATTCAAGCATTCGCGTGCGGCGGGAGATTCAAGCGAGGAGGCGTGAAGCAAGCAAGCAAGCGCGTGGCGTGCGGCGGGAGAAGCAAGCGCGTGATTCGAGCGGGCGTGCGGAAGCGAGCGG"
text3 = "CTTTACTTTAAGGCGTTACTTAGTGCACAGTTTGTATACAGGTATACAGGTATACAGAGGCGTAGGCGTGCACAGTTTCTTTAGCACAGTTTGCACAGTTTAGGCGTTACTTAGTGTATACAGCTTTAAGGCGTTACTTAGTCTTTACTTTAGCACAGTTTGTATACAGGCACAGTTTCTTTAAGGCGTGTATACAGGTATACAGCTTTACTTTATACTTAGTTACTTAGTCTTTAGCACAGTTTCTTTAGCACAGTTTTACTTAGTCTTTAGTATACAGGCACAGTTTGTATACAGGCACAGTTTCTTTAGTATACAGCTTTAGTATACAGGTATACAGGCACAGTTTGTATACAGGTATACAGAGGCGTGTATACAGCTTTAGCACAGTTTTACTTAGTTACTTAGTTACTTAGTGTATACAGTACTTAGTGTATACAGTACTTAGTGCACAGTTTGCACAGTTTCTTTACTTTAAGGCGTGTATACAGCTTTACTTTACTTTATACTTAGTGTATACAGAGGCGTCTTTATACTTAGTGTATACAGGCACAGTTTAGGCGTCTTTAGCACAGTTTAGGCGTTACTTAGTCTTTACTTTAGCACAGTTTGTATACAGAGGCGTAGGCGTAGGCGTGCACAGTTTGCACAGTTTAGGCGTGTATACAGGTATACAGCTTTAGCACAGTTTAGGCGTGTATACAGCTTTAGCACAGTTTGTATACAGAGGCGTAGGCGTTACTTAGTGTATACAGGTATACAGAGGCGTTACTTAGTCTTTAGCACAGTTTTACTTAGTAGGCGTTACTTAGTTACTTAGTAGGCGTGCACAGTTTGCACAGTTTTACTTAGTGTATACAGAGGCGTAGGCGTTACTTAGT"

# Counter
# length

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


cnt = find_frequent_words(text, 4)
print("Matching n-mers: " + " ".join(sorted(cnt)))