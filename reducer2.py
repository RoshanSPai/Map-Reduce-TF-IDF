#!/usr/bin/env python

from operator import itemgetter
import sys

current_file_name = None
current_count = 0
file_count = {}
list=[]

# input comes from STDIN
for line in sys.stdin:
	# remove leading and trailing whitespace
	line = line.strip()
	list.append(line)
	# parse the input we got from mapper.py
	var2, var1 = line.split(',')
	var3, file_name = var2.split('=')
	file_name=file_name.strip()
	var1=var1.strip()
	var4,count = var1.split('&')
	var5,word=var4.split('=')
	word=word.strip()
	count=count.strip()

	# convert count (currently a string) to int
	try:
		count = int(count)
		word_count = count
	except ValueError:
		# count was not a number, so silently
		# ignore/discard this line
		continue

	# this IF-switch only works because Hadoop sorts map output
	# by key (here: word) before it is passed to the reducer
	if current_file_name == file_name:
		current_count += count
	else:
		if current_file_name:
			# write result to STDOUT
			file_count[current_file_name]= current_count
			#print current_file_name + "," + str(file_count[current_file_name])
		current_count = count
		current_file_name = file_name

# do not forget to output the last word if needed!
if current_file_name == file_name:
	file_count[current_file_name]= current_count
	#print current_file_name + "," + str(file_count[current_file_name])
	
	
for line in list:
	# remove leading and trailing whitespace
	line = line.strip()

	var2, var1 = line.split(',')
	var3, file_name = var2.split('=')
	file_name=file_name.strip()
	var1=var1.strip()
	var4,count = var1.split('&')
	var5,word=var4.split('=')
	word=word.strip()
	count=count.strip()
	total_file_count=str(file_count[file_name])
	print "key="+word+"&"+file_name+", value="+count+"&"+total_file_count