#!/usr/local/bin/python3

import os, subprocess, shutil

def countbases(DNAseq, threshold):
	DNAseq = DNAseq.lower()
	nobase=[]
	for base in DNAseq:
		if (base != "a") and (base != "t") and (base != "g") and (base != "c"):
			# create a list of the undetermined bases
			nobase.append(base)
	#return(nobase)

	nrnobase = len(nobase)
	if nrnobase <= threshold:
		return("True")
	else:
		return("False")

assert countbases("agatccagatacaggttacnoononnnoagataaaggga", 3) == "False"
assert countbases("agatccagatacaggttacnoononnnoagataaaggga", 30) == "True"


exit()

DNAseq = "agatccagatacaggttacnoononnnoagataaaggga"

threshold = 3

DNAseq = DNAseq.lower()
nobase=[]
for base in DNAseq:
	if (base != "a") and (base != "t") and (base != "g") and (base != "c"):
		# create a list of the undetermined bases
		nobase.append(base)
print(nobase)

nrnobase = len(nobase)

if nrnobase <= threshold:
	print("True")
else:
	print("False")
