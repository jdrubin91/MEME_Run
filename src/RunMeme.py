__author__ = 'Jonathan Rubin'

#Runs MEME on a fasta formatted list of intervals

import os

def run(fastafile):
    os.system("meme " + fastafile + " -maxsize 10000000 -dna")
    