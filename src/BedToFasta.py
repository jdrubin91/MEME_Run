__author__ = 'Jonathan Rubin'

#Converts an interval bed file into fasta format
import os

def run(intervalfile,fastapath,filedir):
    os.system("bedtools getfasta -fi " + fastapath + " -bed " + intervalfile + " -fo " + filedir + "/out.fasta")
    
    return filedir + "/out.fasta"