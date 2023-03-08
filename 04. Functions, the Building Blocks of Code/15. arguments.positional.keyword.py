# arguments.positional.keyword.py
def func(a, b, c):
	print(a, b, c)

func(42, b = 1, c = 2)

# the following call to func() will not work since positional arguments must
# come before keyword arguments (uncomment to see for yourself)
# func(b = 1, c = 2, 42) # positional argument after keyword arguments