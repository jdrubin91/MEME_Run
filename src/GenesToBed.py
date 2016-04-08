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
    genelist = ['FOSL1', 'ADSL', 'PACRGL', 'SNAPC3', 'EPT1', 'PACRGL', 'SLA2', 'MRPS17', 'CNPY3', 'BRD2', 'KIAA1967', 'SCYL2', 'MED29', 'PTDSS1', 'ZC3H15', 'SLC4A5', 'TBRG1', 'ZCCHC2', 'UBE2D2', 'PACRGL', 'RHBDD2', 'ACADVL', 'RALA', 'SCAMP2', 'SMAP1', 'UHRF1', 'SLC25A44', 'DEF8', 'DEPDC5', 'PSMD2', 'C8orf59', 'MED26', 'MOSPD1', 'RPS6KA4', 'UMPS', 'ERCC4', 'C16orf70', 'PTPN12', 'CEP192', 'OASL', 'YY1', 'PRMT1', 'CMAS', 'SERF1B', 'CCDC66', 'SORBS3', 'ACOT13', 'INTS3', 'SLA2', 'NECAP2', 'C5orf24', 'CDK5RAP3', 'OSGIN2', 'DEF8', 'KIAA1919', 'DCAF13', 'C6orf48', 'PDCD5', 'C5orf24', 'FANCD2', 'TBRG1', 'BMS1P6', 'RNF135', 'C7orf26', 'NDUFB2', 'ZNF326', 'CLPTM1', 'CCDC61', 'WRNIP1', 'DUSP14', 'KLHL7', 'BMP2K', 'UBE2D1', 'ADRM1', 'DAP3', 'HNRNPH3', 'ZBTB4', 'DARS2', 'ATXN7L2', 'C15orf39', 'C8orf59', 'SMAP1', 'DGCR8', 'C8orf59', 'HNRNPAB', 'SEC24A', 'ORAI1', 'ARPC4', 'ATP6V0C', 'DHX33', 'HSPA4', 'CCDC66', 'COX6B1', 'RPL10', 'RNF135', 'TUBB3', 'DNAJA1', 'KHDRBS1', 'NDUFAF5', 'VMA21', 'PSME3', 'SEPT2', 'RNF135', 'NOP56', 'ACTR2', 'CSTF1', 'ASNSD1', 'BRD2', 'MECP2', 'UMPS', 'POLR2M', 'PRMT1', 'OASL', 'TUBB6', 'ADRM1', 'NECAP2', 'LOC100505761', 'DHX33', 'RBM38', 'ME2', 'NSA2', 'NECAP2', 'PCTP', 'C5orf56', 'POLB', 'FAM83D', 'RBCK1', 'SEC24C', 'ACADVL', 'CMPK1', 'SYS1-DBNDD2', 'RBM38', 'SPDL1', 'IDH3A', 'RNF207', 'MVK', 'LRRC8B', 'RPA1', 'ATP6V0C', 'ELAC1', 'UMPS', 'FAM178A', 'LOC100505761', 'RBBP6', 'PSME3', 'SERF1A', 'FAM178A', 'PANK2', 'RPL10', 'WRNIP1', 'RPL10', 'RHBDD2', 'PACRGL', 'DAP3', 'DAP3', 'C6orf48', 'RPL7L1', 'BRMS1', 'C6orf48', 'ADAT3', 'DMWD', 'FADD', 'EMC10', 'PRMT1', 'XRN2', 'LOC100996307', 'BRMS1', 'MRPL45', 'ME2', 'ATXN7L3B', 'ACOT13', 'RAVER1', 'LRRC8A', 'POLH', 'SEPW1', 'DYNLL2', 'ACADVL', 'ADSL', 'LOC654433', 'DEF8', 'PRMT1', 'CREM', 'CAPNS1', 'PTPN12', 'CMPK1', 'OASL', 'DEPDC5', 'C1GALT1', 'CCDC66', 'NOP56', 'CPSF2', 'C8orf59', 'MSRB2', 'ARPC4', 'DAP3', 'MRC2', 'POLR2M', 'PACRGL', 'NDUFAF5', 'CBLL1', 'ACTR2', 'HNRNPH3', 'DEPDC5', 'UBE2D1', 'ZDHHC17', 'LOC100505782', 'C6orf48', 'NDUFAF5', 'RPS6KA4', 'MAP7D1', 'SEC24C', 'DGCR8', 'DAP3', 'CAPNS1', 'UBE2D2', 'CBLL1', 'KLHL7', 'KIAA1033', 'POLR2M', 'RBCK1', 'NME2', 'PSME3', 'CMPK1', 'MRPL44', 'MVK', 'SEPT2', 'EMC10', 'C12orf45', 'LRCH3', 'PSME3', 'LOC284837', 'ARPC4', 'HNRNPAB', 'BMS1P2']
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
        