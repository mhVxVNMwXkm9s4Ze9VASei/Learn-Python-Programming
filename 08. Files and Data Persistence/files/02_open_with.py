# files/open_with.py
with open('fear.txt', encoding = "utf8") as fh:
	for line in fh:
		print(line.strip())
