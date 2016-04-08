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
    genelist = ['PIP5K1A', 'GPR126', 'PMM2', 'LAMB3', 'YWHAZ', 'ATP1A1', 'OSMR', 'PCBP2', 'SERF2-C15ORF63', 'UBE2K', 'CAV1', 'SUPT6H', 'PIP5K1A', 'ARPC4-TTLL3', 'DOT1L', 'GPR126', 'GPR126', 'PIP5K1A', 'FAM208B', 'ATXN10', 'MAPRE2', 'CAPN12', 'SAMD4A', 'UBE2K', 'FUS', 'PCBP2', 'GPR126', 'PPP2R2A', 'FNDC3A', 'PCBP2', 'PCBP2', 'CUL4A', 'RELB', 'TRA2B', 'PCBP2', 'LOC100630923', 'PTPN11', 'PVRL2', 'ALG13', 'SUN1', 'LAMB3', 'SUN1', 'TRA2B', 'YWHAZ', 'UBE2K', 'PIP5K1A', 'FUS', 'ALG13', 'FUS', 'LAMC1', 'PFKP', 'PCBP2', 'PCBP2', 'CAV1', 'LAMB3', 'PAFAH1B1', 'WAC', 'SAMD4A', 'ATXN10', 'TPM4', 'CTPS1', 'FUS']
    #up = ['SLC11A2','TLE3','ITGB8','TNFSF18','DCUN1D3','CCNB1IP1','TUFT1']
    #down = ['AP3M1','HMGA1','GRAMD1B','FLNC','RMRP']
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
        