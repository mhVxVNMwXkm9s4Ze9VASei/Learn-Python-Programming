# pythagorean.triple.generation.py
from functions import gcd
N = 50

triples = sorted(
	(
		(a, b, c) for a, b, c in (							# 1
			((m * m - n * n), (2 * m * n), (m * m + n * n)) # 2
			for m in range(1, int(N ** .5) + 1)				# 3
			for n in range(1, m)							# 4
			if (m - n) % 2 and gcd(m, n) == 1				# 5
		) if c <= N											# 6
	), key = sum											# 7
)

print(triples)
