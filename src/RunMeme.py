__author__ = 'Jonathan Rubin'

#Runs MEME on a fasta formatted list of intervals

import os

def run(fastafile,fastafile1):
    #os.system("meme " + fastafile + " -maxsize 10000000 -dna")
    os.system("dreme -dna -p " + fastafile + " -n " + fastafile1)
    