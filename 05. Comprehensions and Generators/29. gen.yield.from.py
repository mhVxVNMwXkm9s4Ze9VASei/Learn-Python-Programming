# gen.yield.from.py
def print_squares(start, end):
	yield from (n * n for n in range (start, end))

for n in print_squares(2, 8):
	print(n)
