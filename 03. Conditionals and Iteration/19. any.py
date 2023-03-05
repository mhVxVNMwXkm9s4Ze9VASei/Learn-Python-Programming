items = [0, None, 0.0, True, 0, 7] # True and 7 evaluate to True

found = False # this is called "flag"
for item in items:
	print('Scanning item', item)
	if item:
		found = True # we update the flag
		break

if found: # we inspect the flag
	print('At least one item evaluates to true')
else:
	print('All items evaluate to False')