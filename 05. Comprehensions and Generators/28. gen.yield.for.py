# gen.yield.for.py
def print_squares(start, end):
	for n in range (start, end):
		yield n * n

for n in print_squares(2, 8):
	print(n)
