#!/usr/bin/env python

from operator import itemgetter
import sys

current_word = None
current_count = 0
word = None
file_count = {}
list=[]

# input comes from STDIN
for line in sys.stdin:
	# remove leading and trailing whitespace
	line = line.strip()
	list.append(line)
	# parse the input we got from mapper.py
	var2, var1 = line.split(',')
	var3, word = var2.split('=')
	word=word.strip()
	var4= var1.split("&")
	count=var4[3]
	count=count.strip()

	# convert count (currently a string) to int
	try:
		count = int(count)
	except ValueError:
		# count was not a number, so silently
		# ignore/discard this line
		continue

	# this IF-switch only works because Hadoop sorts map output
	# by key (here: word) before it is passed to the reducer
	if current_word == word:
		current_count += count
	else:
		if current_word:
			# write result to STDOUT
			file_count[current_word]= current_count
		current_count = count
		current_word = word

# do not forget to output the last word if needed!
if current_word == word:
	file_count[current_word]= current_count
	
	
for line in list:
	# remove leading and trailing whitespace
	line = line.strip()

	var2, var1 = line.split(',')
	var3, word = var2.split('=')
	word=word.strip()
	var4, var5= var1.split("=")
	value = var5.split("&")
	file_name= value[0]
	n= value[1]
	total=value[2]
	
	total_file_count=str(file_count[word])
	print "key="+word+"&"+file_name+", value="+n+"&"+total+"&"+total_file_count