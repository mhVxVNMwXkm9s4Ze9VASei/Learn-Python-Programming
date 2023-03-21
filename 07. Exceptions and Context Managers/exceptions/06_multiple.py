# exceptions/multiple.py
values = (1, 0)

try:
	q, r = divmod(*values)
except (ZeroDivisionError, TypeError) as e:
	print(type(e), e)

try:
	q, r = divmod(*values)
except ZeroDivisionError:
	print("You tried to divide by zero!")
except TypeError as e:
	print(e)
