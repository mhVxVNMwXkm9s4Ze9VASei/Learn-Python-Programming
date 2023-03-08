# arguments.keyword.py
def func(a, b, c):
	print(a, b, c)

func(a = 1, c = 2, b = 3) # prints 1 3 2
func(b = 1, a = 2, c = 3)
func(c = 1, a = 2, b = 3)
func(b = 1, c = 2, a = 3)