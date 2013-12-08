#!/bin/src/python
import vcf
import pymongo 
import dictMap

class UpdateVcfMongo:

	vcf_reader = vcf.Reader(open('/data/analysis/CasanovaJL/Project_CAS_01015_Exome_2013-09-26/Sample_JL1452/analysis/JL1452.variantCalls.vcf','r'))
	
	def _init_(self):
		#self.vcf_reader = vcf_reader
		global vcf_reader 
	
	def ConnectToMongo(self):
		from pymongo import Connection
		connection = Connection()
		db = connection.test
		vcfColl = db.VCF
		return vcfColl
		
	def InsertIntoVcfMongo(self):
		vcf_reader = self.vcf_reader	
		from dicMap import DictMap
                dinst = DictMap() 
		vcfColl = self.ConnectToMongo()
	 	for r in vcf_reader:
			l = len(r.samples)
			for i in range(l):									vcfColl.insert({'Sample_ID':r.samples[i].sample,'CHROM':r.CHROM,'POS':r.POS,'REF':r.REF})	
		return vcfColl
	
	def UpsertIntoVcfMongo(self):
		vcf_reader = self.vcf_reader
		from dictMap import DictMap
                dinst = DictMap()
                vcfColl = self.ConnectToMongo()
                for r in vcf_reader:
                        l = len(r.samples)
			arr = r.ALT
			f = dinst.my(arr)
			d = dinst.dToString(f)
                        for i in range(l):
				vcfColl.update({'Sample_ID':r.samples[i].sample,'CHROM':r.CHROM,'POS':r.POS},{'$set':{'QUAL':r.QUAL}}, upsert = True, multi =  True )
				vcfColl.update({'Sample_ID':r.samples[i].sample,'CHROM':r.CHROM,'POS':r.POS},{'$set': d }, upsert = True, multi =  True )
				                       
                return vcfColl
	
	def UpsertFormatVcfMongo(self):
		vcf_reader = self.vcf_reader
                vcfColl = self.ConnectToMongo()
                for r in vcf_reader:
			FormatKeys = r.FORMAT.split(":")
			sampleSets = r.samples
			l = len(sampleSets)
                        for i in range(l):
				FormatValues = []
				singleSampleSet = sampleSets[i]
				for eachV in singleSampleSet.data:
					FormatValues.append(eachV)
					FormatMap = dict(zip(FormatKeys,FormatValues))	
                       		vcfColl.update({'Sample_ID':singleSampleSet.sample,'CHROM':r.CHROM,'POS':r.POS},FormatMap, upsert = True, multi =  True )
                return vcfColl

	def UpsertInfoVcfMongo(self):
		vcf_reader = self.vcf_reader
                vcfColl = self.ConnectToMongo()
		for r in vcf_reader:
			infoD = {}
			for eachInfoK in r.INFO:
				if eachInfoK in ('FS','MQ','MQ0','QD'):
					infoD[eachInfoK] = r.INFO.get(eachInfoK)
			sampleSets = r.samples
                        l = len(sampleSets)
			for i in range(l):
				vcfColl.update({'Sample_ID':r.samples[i].sample,'CHROM':r.CHROM,'POS':r.POS},{'$set': infoD }, upsert = True, multi =  True )
		return vcfColl

	def PrintVcfInsert(self):
		result = self.InsertIntoVcfMongo()
		for p in result.find():
			print p 
     		
	def PrintVcfUpsert(self):
                result = self.UpsertIntoVcfMongo()
                for p in result.find():
                        print p             		
	             		
	def PrintVcfUpsertFormat(self):
		result = self.UpsertFormatVcfMongo()
		for p in result.find():
			print p
	
	def PrintVcfUpsertINFO(self):
                result = self.UpsertInfoVcfMongo()
                for p in result.find():
                        print p             		
