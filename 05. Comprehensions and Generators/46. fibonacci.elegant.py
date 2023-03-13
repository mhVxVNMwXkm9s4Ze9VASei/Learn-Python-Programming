# fibonacci.elegant.py
def fibonacci(N):
	"""Return all fibonacci numbers up to N."""
	a, b = 0, 1
	while a <= N:
		yield a
		a, b = b, a + b

print(list(fibonacci(50)))