#!/usr/bin/env python

import sys
import os

# input comes from STDIN (standard input)
for line in sys.stdin:
	# remove leading and trailing whitespace
	line = line.strip()
	# split the line into words
	keys,value=line.split(",")
	first,file_name=keys.split("&")
	var1,word=first.split("=")
	words = line.split()
	var2,count=value.split("=")
	file_name=file_name.strip()
	word=word.strip()
	count=count.strip()
	# increase counters
	#for word in words:
		# write the results to STDOUT (standard output);
		# what we output here will be the input for the
		# Reduce step, i.e. the input for reducer.py
		#
		# tab-delimited; the trivial word count is 1
	print 'key=%s,value=%s&%s' % (file_name, word,count)
