# decorates/syntax.py
def func(arg1, arg2, arg3):
	pass
func = decorator(func)

# is equivalent to the following
@decorator
def func(arg1, arg2, arg3):
	pass

####

func = deco1(deco2(func))

# is equivalent to the following
@deco1
@deco2
def func(arg1, arg2, arg3):
	pass

####

func = decoarg(arg_a, arg_b, arg_c)(func)

# is equivalent to the following
@decoarg(arg_a, arg_b)
def func(arg1, arg2, arg3):
	pass
