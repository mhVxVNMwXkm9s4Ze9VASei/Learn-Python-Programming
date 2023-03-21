# first.n.squares.manual.py
def get_squares_gen(n):
	for x in range(n):
		yield x * x

squares = get_squares_gen(4) # this creates a generator object
print(squares) # <generator object get_squares_gen ...>
print(next(squares)) # prints 0
print(next(squares)) # prints 1
print(next(squares)) # prints 4
print(next(squares)) # prints 9
# the following raises StopIteration. The generator is exhausted.
# any further call to next will keep raising StopIteration
print(next(squares))