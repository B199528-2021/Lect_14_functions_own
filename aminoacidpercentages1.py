#!/usr/local/bin/python3

import os, subprocess, shutil

#protseq = "MSRSLLLRFLLFLLLLPPLP"
#aminoacid = "M"

#percentage = 100*( protseq.count(aminoacid) / len(protseq) )

#print(percentage)

def calcpercentage(protseq, aminoacid):
	aminoacid = aminoacid.upper()
	percentage = 100*( protseq.count(aminoacid) / len(protseq) )
	return(percentage)

assert round(calcpercentage("MSRSLLLRFLLFLLLLPPLP", "M")) == round(5)
assert round(calcpercentage("MSRSLLLRFLLFLLLLPPLP", "r")) == round(10)
assert round(calcpercentage("MSRSLLLRFLLFLLLLPPLP", "L")) == round(50)
assert round(calcpercentage("MSRSLLLRFLLFLLLLPPLP", "Y")) == round(0)
