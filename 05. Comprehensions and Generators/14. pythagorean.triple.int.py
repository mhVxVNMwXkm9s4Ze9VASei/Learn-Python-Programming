# pythagorean.triple.int.py
from math import sqrt
mx = 10
triples = [(a, b, sqrt(a * a + b * b)) for a in range(1, mx) for b in range (a, mx)]
triples = filter(lambda triple: triple[2].is_integer(), triples)

# this will make the third number in the tuples an integer
triples = list(map(lambda triple: triple[:2] + (int(triple[2]), ), triples))

print(triples) # prints [(3, 4, 5), (6, 8, 10)]
