# squares.map.py
# If you code like this, you are not a Python dev! ;)

squares = []
for n in range(10):
	squares.append(n * n)

print(squares)

# This is better. One line; nice and readable.
squares = map(lambda n: n * n, range(10))
print(list(squares))
