#!/bin/src/python

import vcf
import updateVcfMongo
import glob
import os

from vcfGT import vcfGT

directory = r"./files/*.vcf"

for path in glob.glob(directory):
	vcf_reader = vcf.Reader(open(path,'r'))
	ex = vcfGT(vcf_reader)
	ex.InsertIntoGT()

