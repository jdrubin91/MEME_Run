__author__ = 'Jonathan Rubin'

#Converts an interval bed file into fasta format
import os

def run(intervalfile,intervalfile2,fastapath,filedir):
    os.system("bedtools getfasta -fi " + fastapath + " -bed " + intervalfile + " -fo " + filedir + "/out.fa")
    os.system("bedtools getfasta -fi " + fastapath + " -bed " + intervalfile2 + " -fo " + filedir + "/out2.fa")
    
    return filedir + "/out.fa",filedir + "/out2.fa"