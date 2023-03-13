# gen.map.filter.py
N = 20
cubes1 = map(
	lambda n: (n, n * n * n),
	filter(lambda n: n % 3 == 0 or n % 5 == 0, range(N))
)
cubes2 = ((n, n * n * n) for n in range(N) if n % 3 == 0 or n % 5 == 0)

print(list(cubes1))
print(list(cubes2))
