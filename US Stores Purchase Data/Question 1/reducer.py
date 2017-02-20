#!/usr/bin/python

import sys

salesTotal = 0
oldKey = None

# Loop around the data
# It will be in the format key\tval
# Where key is the item category, val is the sale amount
#
# All the sales for a particular item category will be presented,
# then the key will change and we'll be dealing with the category

for line in sys.stdin:
	data = line.strip().split("\t")
    	if len(data) != 2:
        # Something has gone wrong. Skip this line.
        	continue

    	thisItem, thisSale = data

	if thisItem == 'Toys' or thisItem == 'Consumer Electronics':
		# Skip all the data whose category is not Toys or Consumer Electronic.

	    	if oldKey and oldKey != thisItem:
			print oldKey, "\t", salesTotal
			salesTotal = 0

	    	oldKey = thisItem
	    	salesTotal += float(thisSale)
        
# Print out the last key
if oldKey != None:
	print oldKey, "\t", salesTotal
