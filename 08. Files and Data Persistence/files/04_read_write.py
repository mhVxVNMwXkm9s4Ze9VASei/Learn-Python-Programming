# files/read_write.py
with open('fear.txt', encoding = 'utf8') as f:
	lines = [line.rstrip() for line in f]

with open('fear_copy.txt', 'w') as fw:
	fw.write('\n' . join(lines))
