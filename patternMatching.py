__author__ = 'rob'

pattern = "ATAT"
genome = "GATATATGCATATACTT"
#pattern = "CTTGATCAT"
#genome = ""

from week1_library import allindices


#with open('genome.txt', 'r') as f:
#    genome = f.read()

matchingIndices = allindices(genome, pattern)
print(str(matchingIndices).strip('[]').replace(',', ''))
