#!/usr/bin/python
class DictMap:
	#def _init_(self):
		 
	def my(self,arr):
		keys = [];vals =[]
		for i in range(len(arr)):
			keys.append('ALT'+str(i+1));vals.append(arr[i])
		elt = dict(zip(keys,vals))
		return elt
	
	def m(self,arr):
		d={}
		for i in range(len(arr)):
			d['ALT'+str(i+1)] = arr[i]
		return d
	
	def dToString(self,d):
		for k in d:
			d[k] = str(d[k])
		return d 
