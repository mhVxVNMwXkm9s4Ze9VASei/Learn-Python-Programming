# return.single.value.2.py
from functools import reduce
from operator import mul

def factorial(n):
	return reduce(mul, range(1, n + 1), 1)

print(factorial(12))