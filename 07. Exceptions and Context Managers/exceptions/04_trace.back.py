# exceptions/trace.back.py
def squareroot(number):
	if number < 0:
		raise ValueError("No negative numbers, please.")
	return number ** .5

def quadratic(a, b, c):
	d = b * b - 4 * a * c
	return (
		(-b - squareroot(d)) / (2 * a),
		(-b + squareroot(d)) / (2 * a)
	)

print(quadratic(1, 0, 1)) # x**2 + 1 == 0
