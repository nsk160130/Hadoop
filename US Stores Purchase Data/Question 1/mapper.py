#!/usr/bin/python

# Format of each line is:
# date\ttime\tstore name\titem description\tcost\tmethod of payment
#
# This time we want two different elemetns: Item category and the Cost
# We need to write them out to standard output, separated by a tab, so the reducer can read it from standard input.


import sys

for line in sys.stdin:
	data = line.strip().split("\t")
	
	if len(data) != 6:
		continue

	date,time,store,item,cost,payment = data
	print "{0}\t{1}".format(item,cost)   ## Print out the Item category and the cost.
