# custom.py
def debug(*msg, print_separator = True):
	print(*msg)
	if print_separator:
		print('-' * 40)

debug('Data is ...')
debug('Different', 'Strings', 'Are', 'Not', 'A', 'Problem')
debug('After while loop', print_separator = False)
