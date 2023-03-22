# files/open_try.py
# fh = open('fear.txt', 'rt') # r: read, t: text

# for line in fh.readlines():
# 	print(line.strip()) # remove whitespace and print

# fh.close()

# try:
# 	for line in fh.readlines():
# 		print(line.strip())
# finally:
# 	fh.close()

fh = open('fear.txt', encoding = 'utf8') # rt is default

try:
	for line in fh: # we can iterate directly on fh
		print(line.strip())
finally:
	fh.close()
