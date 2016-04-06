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
    #genelist = ['SLC11A2','TLE3','ITGB8','TNFSF18','AP3M1','HMGA1','DCUN1D3','CCNB1IP1','GRAMD1B','LOC100131060','FLNC,RMRP','TUFT1']
    genelist = ['SLC11A2','TLE3','ITGB8','TNFSF18','DCUN1D3','CCNB1IP1','TUFT1']
    down = ['AP3M1','HMGA1','GRAMD1B','FLNC','RMRP']
    file1 = filedir + '/refFlat_hg19.bed'
    file2 = filedir + '/refGene.bed'
    file3 = filedir + '/RefSeqHG19.bed'
    window = 200
    
    d1 = dict()
    
    with open(file1) as F1:
        for line in F1:
            chrom,start,stop,gene = line.strip().split()[0:4]
            if not gene in d1:
                d1[gene] = chrom + '\t' + str(int(start)-200) + '\t' + str(int(start)+200) + '\n'
                
    with open(file2) as F2:
        for line in F2:
            chrom,start,stop,gene = line.strip().split()[0:4]
            gene1,gene2 = gene.split(';')[0:2]
            if not gene1 in d1:
                d1[gene1] = chrom + '\t' + str(int(start)-200) + '\t' + str(int(start)+200) + '\n'
            if not gene2 in d1:
                d1[gene2] = chrom + '\t' + str(int(start)-200) + '\t' + str(int(start)+200) + '\n'
                
    with open(file3) as F3:
        for line in F3:
            chrom,start,stop,gene = line.strip().split()[0:4]
            if not gene in d1:
                d1[gene] = chrom + '\t' + str(int(start)-200) + '\t' + str(int(start)+200) + '\n'
    
    outfile = open(filedir + '/GenesToBed.bed','w')
    for gene in genelist:
        if gene in d1:
            outfile.write(d1[gene])
    outfile2 = open(filedir +'/GenesToBed_cntrl.bed','w')
    for gene in d1:
        if not gene in genelist:
            outfile2.write(d1[gene])
        