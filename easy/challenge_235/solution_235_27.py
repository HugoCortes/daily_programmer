from math import ceil, sqrt
import re

def PrimeFactors(n):
    if n <= 1: return []
    # Next grabs the next value or n if condition is not met
    prime = next((x for x in range(2, int(ceil(sqrt(n))+1)) if n%x == 0), n)  
    return [prime] + PrimeFactors(n/prime)

with open("input_1.in") as fileInput:
    print "Ruth Aaron Pair Problem"
    try:
        for i, line in enumerate(fileInput):
            lineMatch = re.match( '\((\d+),(\d+)\)', line, re.M | re.I)
            if lineMatch:
                first  = int(lineMatch.group(1))
                second = int(lineMatch.group(2))
                primeSumN = sum(sorted(set(PrimeFactors(first))))
                primeSumM = sum(sorted(set(PrimeFactors(second))))
                print (primeSumN,primeSumM), 'VALID' if primeSumN == primeSumM else 'NOT VALID'
    finally:
        fileInput.close()
