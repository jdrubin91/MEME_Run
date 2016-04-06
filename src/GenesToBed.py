__author__ = 'Jonathan Rubin'

#Creates bed file of locations from gene names

import os

#Return parent directory
def parent_dir(directory):
    pathlist = directory.split('/')
    newdir = '/'.join(pathlist[0:len(pathlist)-1])
    
    return newdir

#Home directory
homedir = os.path.dirname(os.path.realpath(__file__))

#File directory
filedir = 'C:/cygwin64/home/Jonathan/MEME_Run/files'

if __name__ == "__main__":
    genelist = ['SLC11A2','TLE3','ITGB8','TNFSF18','AP3M1','HMGA1','DCUN1D3','CCNB1IP1','GRAMD1B','LOC100131060','FLNC,RMRP','TUFT1']
    file1 = filedir + '/refFlat_hg19.bed'
    file2 = filedir + '/refGene.bed'
    file3 = filedir + '/RefSeqHG19.bed'
    
    d1 = dict()
    
    with open(file1) as F1:
        for line in F1:
            chrom,start,stop,gene = line.strip().split()[0:4]
            if not gene in d1:
                d1[gene] = chrom + '\t' + start + '\t' + stop + '\n'
                
    with open(file2) as F2:
        for line in F2:
            chrom,start,stop,gene = line.strip().split()[0:4]
            gene1,gene2 = gene.split(';')[0:2]
            if not gene1 in d1:
                d1[gene1] = chrom + '\t' + start + '\t' + stop + '\n'
            if not gene2 in d1:
                d1[gene2] = chrom + '\t' + start + '\t' + stop + '\n'
                
    with open(file3) as F3:
        for line in F3:
            chrom,start,stop,gene = line.strip().split()[0:4]
            if not gene in d1:
                d1[gene] = chrom + ':' + start + '-' + stop
    
    outfile = open(filedir + '/GenesToBed.bed','w')
    for gene in genelist:
        if gene in d1:
            outfile.write(d1[gene])