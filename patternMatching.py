__author__ = 'rob'

#pattern = "ATAT"
#genome = "GATATATGCATATACTT"
pattern = "CTTGATCAT"
genome = ""

def allindices(string, sub, listindex=[], offset=0):
    i = string.find(sub, offset)
    while i >= 0:
        listindex.append(i)
        i = string.find(sub, i + 1)
    return listindex

with open('genome.txt', 'r') as f:
    genome = f.read()

matchingIndices = allindices(genome, pattern)
print(str(matchingIndices).strip('[]').replace(',', ''))
