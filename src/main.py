__author__ = 'Jonathan Rubin'

#This package takes as input a list of intervals, converts these to fasta format
#and then runs MEME to identify enriched TF motifs which are then run through
#TOMTOM.  Returns a list of TFs that are enriched in the given interval dataset
#in order of significance.

import os
import BedToFasta
import RunMeme

#Take in full path to file
intervalfile = '/scratch/Users/joru1876/TBX19_DMSO_intersect.bed'

#Full path to genome fasta file
fastapath = '/scratch/Users/joru1876/hg19_all.fa'

#Return parent directory
def parent_dir(directory):
    pathlist = directory.split('/')
    newdir = '/'.join(pathlist[0:len(pathlist)-1])
    
    return newdir

#Home directory
homedir = os.path.dirname(os.path.realpath(__file__))

#File directory
filedir = parent_dir(homedir) + '/files'

#Figure directory
figuredir = parent_dir(homedir) + '/figures'

def run():
    fastafile = BedToFasta.run(intervalfile,fastapath,filedir)
    RunMeme.run(fastafile,filedir)