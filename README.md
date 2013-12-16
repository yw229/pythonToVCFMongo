Pymongo, PyVcf to populate all meta data from VCF files into MongoDB 

All the meta data in each VCF file, under each conlumn are store in VCF collection. 

All the run*.py scripts are for the inserting compound key fileds values, upserting additional parsed columns(e.g: Variants from FORMAT fileds and it's mapping values for per sample, fileds extracted from INFO colunms 'FS','MQ','MQ0','QD' for all samples in each row. )

Another Collection to store all the header information as to per VCF files..  
