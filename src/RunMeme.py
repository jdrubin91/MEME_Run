__author__ = 'Jonathan Rubin'

#Runs MEME on a fasta formatted list of intervals

import os

def run(fastafile,filedir):
    os.system("meme " + fastafile + " -maxsize 1000000")
    