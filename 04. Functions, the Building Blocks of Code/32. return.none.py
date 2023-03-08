# return.none.py
def func():
	pass

func() # the return of this call won't be collected. It's lost.
a = func() # the return of this one is collected into 'a'
print(a) # prints None