#!/usr/bin/python 
import vcf

vcf_reader = vcf.Reader(open('/data/analysis/CasanovaJL/Project_CAS_01015_Exome_2013-09-26/Sample_JL1452/analysis/JL1452.variantCalls.vcf','r'))

print "CHROM","POS","REF","ALT","MQRankSum"
for record in vcf_reader:
	try:
		print (record.CHROM,record.POS,record.REF,record.ALT,record.INFO['MQRankSum'])
	except KeyError:
		continue
		
