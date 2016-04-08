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
    genelist = [' DDX60L',
                'MSMO1',
                'ARPC4',
                'GPR126',
                'SNHG7',
                'POLR2L',
                'RPL14',
                'H2AFX',
                'ABCC3',
                'ZNFX1',
                'GPR113',
                'RPL24',
                'SLC20A2',
                'RNF167',
                'LYRM1',
                'NME2',
                'DMKN',
                'PUS1',
                'PHLDA2',
                'GAPDH',
                'RPS3',
                'CLOCK',
                'SLC39A14',
                'RPSA',
                'ARHGDIA',
                'ARHGDIA',
                'INO80',
                'MCFD2',
                'RPL12',
                'C16orf52',
                'ANKRD28',
                'SERINC4',
                'WDR25',
                'CD68',
                'SQSTM1',
                'SQSTM1',
                'ABCC3',
                'LINC00324',
                'SERF2',
                'TUBB4B',
                'WASH3P',
                'FOS',
                'PLAUR',
                'KANK3',
                'ELP5',
                'ELP5',
                'CHD2',
                'WDR25',
                'RPS3A',
                'RPS17',
                'CFLAR',
                'LOC100128881',
                'RPL11',
                'DUSP8',
                'TFRC',
                'WIPI1',
                'NT5E',
                'EIF4E',
                'CTTN',
                'CREM',
                'PUS1',
                'PUS1',
                'RFC4',
                'FLJ43663',
                'NFE2L1',
                'SERF2',
                'CREM',
                'OGDH',
                'GTF2IRD2',
                'SNHG7',
                'ANKRD30BL',
                'CLCF1',
                'RPS3',
                'RPS3A',
                'RPLP0',
                'ARPC4',
                'RPL28',
                'RPL28',
                'RPS10-NUDT3',
                'NFKB2',
                'WDR45L',
                'FAM166A',
                'BCAM',
                'METTL23',
                'BCL2L2-PABPN1',
                'HGS',
                'MIR22HG',
                'WTAP',
                'RPS29',
                'RPS27',
                'SERF2',
                'INTS6',
                'ACSL5',
                'PPP1R15A',
                'ZBTB38',
                'GNAS',
                'RPS4X',
                'LOC100506233',
                'TRAF4',
                'RPL17-C18ORF32',
                'RPL17-C18ORF32']
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
        