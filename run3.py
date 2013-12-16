import vcf
import updateVcfMongo
import glob
import os

from updateVcfMongo import UpdateVcfMongo

directory = r"./files/*.vcf"
for path in glob.glob(directory):
        vcf_reader = vcf.Reader(open(path,'r'))

        ex = UpdateVcfMongo(vcf_reader)

        #ex.PrintVcfInsert()

        #ex.PrintVcfUpsert()

        ex.PrintVcfUpsertFormat()

        #ex.PrintVcfUpsertINFO()
