# pythagorean.triple.comprehension.py
from math import sqrt

# this step is the same as before
mx = 10
triples = [(a, b, sqrt(a * a + b * b)) for a in range(1, mx) for b in range(a, mx)]

# here we combine filter and map in one CLEAN list comprehension
triples = [(a, b, int(c)) for a, b, c in triples if c.is_integer()]
print(triples)
