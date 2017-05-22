#!/usr/bin/env python

import sys
import os
import math

D=10
# input comes from STDIN (standard input)
for line in sys.stdin:
	# remove leading and trailing whitespace
	line = line.strip()
	# split the line into words
	keys,value=line.split(",")
	first,file_name=keys.split("&")
	var1,word=first.split("=")
	var2,var3=value.split("=")
	values=var3.split("&")
	
	file_name=file_name.strip()
	word=word.strip()
	count=values[0].strip()
	total=values[1].strip()
	m=values[2].strip()
	try:
		count=float(count)
		total=float(total)
		m=float(m)
		tfidf=count/total* math.log(D/m) 
	except ValueError:
		# count was not a number, so silently
		# ignore/discard this line
		continue
	# increase counters
	#for word in words:
		# write the results to STDOUT (standard output);
		# what we output here will be the input for the
		# Reduce step, i.e. the input for reducer.py
		#
		# tab-delimited; the trivial word count is 1
	print 'key=%s&%s,value=%s' % (word,file_name,tfidf)
