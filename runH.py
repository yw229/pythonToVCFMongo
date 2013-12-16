#!/bin/src/python

import vcf
import updateVcfMongo
import glob 
import os 

from updateVcfHeader import UpdateVcfHeader
directory = r"./files/*.vcf"

for path in glob.glob(directory):
		
#vcf_reader = vcf.Reader(open('/data/analysis/CasanovaJL/Project_CAS_01015_Exome_2013-09-26/Sample_JL1452/analysis/JL1452.variantCalls.vcf','r'))
	vcf_reader = vcf.Reader(open(path,'r'))
	ex = UpdateVcfHeader(vcf_reader)

	ex.PrintVcfInsert()
