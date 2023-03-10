# even.squares.py
# using map and filter
sq1 = list(map(lambda n: n * n, filter(lambda n: not n % 2, range(10))))
print(sq1)

# equivalent but using list comprehensions
sq2 = [n * n for n in range(10) if not n % 2]
print(sq2)
