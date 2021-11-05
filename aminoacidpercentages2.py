#!/usr/local/bin/python3

import os, subprocess, shutil

#protseq = "MSRSLLLRFLLFLLLLPPLP"
#aminoacid = ["M","F","R"]

#sumaminoacid=[]
#for aa in aminoacid:
#	sumaminoacid.append(int(protseq.count(aa)))

# calculate the sum of each amino acid
#sumaa = sum(sumaminoacid)

# calculate the percentage
#percentage = 100*( sumaa / len(protseq) )

#print(percentage)

def calcpercentage(protseq, aminoacid=["A", "I", "L", "M", "F", "W", "Y", "V"]):
	sumaminoacid=[]
	for aa in aminoacid:
		sumaminoacid.append(int(protseq.count(aa)))

	# calculate the sum of each amino acid
	sumaa = sum(sumaminoacid)
	
	# calculate the percentage
	percentage = 100*( sumaa / len(protseq) )

	return(percentage)

assert round(calcpercentage("MSRSLLLRFLLFLLLLPPLP", ["M"])) == 5
assert round(calcpercentage("MSRSLLLRFLLFLLLLPPLP", ['F', 'S', 'L'])) == 70
assert round(calcpercentage("MSRSLLLRFLLFLLLLPPLP")) == 65
