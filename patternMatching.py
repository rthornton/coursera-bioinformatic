__author__ = 'rob'

#pattern = "ATAT"
#genome = "GATATATGCATATACTT"
pattern = "CTTGATCAT"

def allindices(string, sub, listindex=[], offset=0):
    i = string.find(sub, offset)
    while i >= 0:
        listindex.append(i)
        i = string.find(sub, i + 1)
    return listindex


matchingIndices = allindices(genome, pattern)
print(str(matchingIndices).strip('[]').replace(',', ''))