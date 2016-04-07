__author__ = 'Jonathan Rubin'

#This package takes as input a list of intervals, converts these to fasta format
#and then runs MEME to identify enriched TF motifs which are then run through
#TOMTOM.  Returns a list of TFs that are enriched in the given interval dataset
#in order of significance.

import os
import BedToFasta
import RunMeme
import RunTomtom

#Take in full path to file
intervalfile = '/scratch/Users/joru1876/MEME_Run/files/GenesToBed.bed'
intervalfile2 = '/scratch/Users/joru1876/MEME_Run/files/GenesToBed_cntrl.bed'

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

#Meme directory
Memedir = parent_dir(homedir) + '/dreme_out'

#HOCOMOCO filepath
databse = filedir + '/HOCOMOCOv10_HUMAN_mono_meme_format.meme'

def run():
    #fastafile,fastafile1 = BedToFasta.run(intervalfile,intervalfile2,fastapath,filedir)
    #RunMeme.run(fastafile,fastafile1)
    RunTomtom.run(Memedir,databse)