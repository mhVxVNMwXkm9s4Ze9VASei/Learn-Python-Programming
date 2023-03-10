# pythagorean.triple.py
from math import sqrt

# this will generate all possible pairs
mx = 10
triples = [(a, b, sqrt(a * a + b * b)) for a in range(1, mx) for b in range(a, mx)]

# this will filter out all non-Pythagorean triples
triples = list(filter(lambda triple: triple[2].is_integer(), triples))

print(triples) # (3, 4, 5.0), (6, 8, 10.0)
