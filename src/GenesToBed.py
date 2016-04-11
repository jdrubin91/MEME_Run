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
    genelist = ['PAXIP1', 'ELOVL1', 'MASTL', 'E4F1', 'C19orf55', 'NUDT22', 'TARBP2', 'RBM42', 'THAP2', 'USB1', 'MPPE1', 'MRPS11', 'HSPA1B', 'CNBP', 'TEX264', 'ZBTB1', 'STRADA', 'LOC100287042', 'LOC100506233', 'PLCB3', 'FSCN1', 'FABP5', 'ATRIP', 'VPS25', 'CNBP', 'RCCD1', 'BICD2', 'ZNF302', 'ALG13', 'JMJD7-PLA2G4B', 'TDP2', 'RAB33B', 'MSL1', 'PLD2', 'MAP3K13', 'MASTL', 'CTBP1-AS1', 'JMJD7-PLA2G4B', 'DZIP3', 'KIAA0753', 'MASTL', 'SERF2', 'MPPE1', 'DRG1', 'EPM2A', 'PSMD2', 'MRPS33', 'MANF', 'STRADA', 'ERCC4', 'OAZ1', 'VDAC3', 'FGD5-AS1', 'UROS', 'TUBB3', 'TUBG1', 'ZNF771', 'FGD5-AS1', 'ZNF720', 'SERF1B', 'DHRS4', 'LPP-AS2', 'GTPBP8', 'LY6E', 'NECAP2', 'C5orf24', 'MPPE1', 'LYPLA1', 'CDK5RAP3', 'GEMIN2', 'TTLL3', 'SIRT5', 'SEC24B-AS1', 'KIAA1919', 'PLD2', 'TOR4A', 'GEMIN2', 'FGD5-AS1', 'ZNF572', 'HSD17B7', 'TMEM5', 'C5orf24', 'LOC100506054', 'STRADA', 'STK36', 'EMC4', 'ALG6', 'ZNF326', 'NUDT22', 'EXOC7', 'CCDC61', 'STRADA', 'KAT8', 'TTLL3', 'UBE2D1', 'RGS10', 'PPCS', 'DAK', 'FAM53C', 'MPPE1', 'ACBD5', 'CNBP', 'SLC35E1', 'SEZ6L2', 'SEZ6L2', 'NBN', 'FAM50A', 'LOC100507173', 'PMS2P5', 'C1orf50', 'ELOVL1', 'SEZ6L2', 'GLRX5', 'BOP1', 'TRMT12', 'ZBTB5', 'SSR4', 'TMEM177', 'PGAM5', 'MRM1', 'ABT1', 'MOV10', 'SEZ6L2', 'DYRK3', 'LOC202781', 'PLEKHO2', 'ABHD5', 'EED', 'MPDU1', 'PIM3', 'SF3B1', 'FEN1', 'ALG13', 'KCTD13', 'C11orf1', 'ADAM15', 'RCCD1', 'PRR14', 'YME1L1', 'YME1L1', 'SFN', 'NECAP2', 'ELOVL1', 'RPL23AP53', 'ACBD5', 'PGLS', 'ASNA1', 'ATRIP', 'ZNF830', 'GTF2IRD2B', 'PTGER4', 'RELT', 'PMS2P5', 'PPP1R9B', 'ARL1', 'GLUD1', 'RIOK2', 'TINF2', 'CNTROB', 'PSMC5', 'GTPBP8', 'NECAP2', 'FAM83D', 'LOC285033', 'WDR67', 'C1orf50', 'SERF2', 'ASAH2B', 'CHRAC1', 'LOC284385', 'EXOC7', 'SEC23A', 'RPL26L1', 'SERF2', 'EXOC7', 'GFER', 'GMPPA', 'ITFG2', 'SEZ6L2', 'CLN5', 'SCO1', 'ATP6V1F', 'ARID3B', 'DEAF1', 'NGRN', 'JMJD7', 'FGD5-AS1', 'KLF2', 'SERF1A', 'TCAIM', 'NAGLU', 'GPATCH1', 'BICD2', 'PABPC1L', 'BLOC1S2', 'EXOC7', 'JOSD1', 'LOC100131496', 'SERF2', 'LOC100507173', 'SLX1A', 'MPDU1', 'DVL1', 'TMEM208', 'GMPPA', 'HERPUD1', 'CNTROB', 'CNBP', 'CNBP', 'MRPL45', 'ETFB', 'PIGV', 'LEPREL2', 'ELOVL1', 'PCK2', 'RNF25', 'TSGA10', 'APEH', 'LRRC8A', 'STRADA', 'IMP4', 'CNBP', 'NDUFAF3', 'ZNF259', 'SELT', 'WBP1L', 'DYNLL2', 'PVRL1', 'NUDT22', 'GEMIN2', 'PEX11B', 'PCK2', 'EXOSC4', 'SLX1A', 'TEX264', 'HERPUD1', 'EED', 'ARF5', 'SH3BGRL3', 'DYRK3', 'C7orf73', 'SLC16A6', 'SSR4', 'PLCB3', 'TEX264', 'TMEM177', 'SLX1B', 'SLX1B', 'VDAC3', 'CYB561', 'PEX11B', 'RIOK1', 'PPP3R1', 'STK36', 'ZNF771', 'UQCR10', 'SNHG11', 'NGRN', 'PPCS', 'PRKRA', 'SWI5', 'BAG2', 'UBE2D1', 'EPM2A', 'ALG13', 'NDUFAF3', 'DUSP28', 'C15orf37', 'EXOC7', 'DHX29', 'TINF2', 'FPGS', 'ZNF302', 'TEX264', 'SERF2', 'LY6E', 'WDR55', 'UQCR10', 'LOC100506054', 'C3orf37', 'LOC100506054', 'PLEKHO2', 'SUV420H1', 'CLNS1A', 'STRADA', 'SEZ6L2', 'TARBP2', 'ZNF330', 'ATP6V1F', 'C4orf52', 'MPPE1', 'MOV10', 'YME1L1', 'KAT8', 'UNC45A', 'CECR5', 'POR', 'KLHL7', 'WDR67', 'VASN', 'TMEM177', 'POLR3D', 'SLC16A6', 'SSR4', 'NFE2L1', 'CYC1', 'MRPS11', 'PVRL1', 'KLHL7', 'ATRIP', 'LINC00339', 'RIPK2', 'HERPUD1', 'THAP6']
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
        