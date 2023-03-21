# context/decimal.prec.py
from decimal import Context, Decimal, getcontext, setcontext

# one = Decimal("1")
# three = Decimal("3")

# orig_ctx = getcontext()
# ctx = Context(prec = 5)
# setcontext(ctx)
# print(ctx)
# print(one / three)
# setcontext(orig_ctx)
# print(one / three)

one = Decimal("1")
three = Decimal("3")
# orig_ctx = getcontext()
# ctx = Context(prec = 5)
# setcontext(ctx)
# try:
# 	print(ctx)
# 	print(one / three)
# finally:
# 	setcontext(orig_ctx)
# print(one / three)

from decimal import localcontext

# with localcontext(Context(prec = 5)) as ctx:
# 	print(ctx)
# 	print(one / three)
# print(one / three)

with localcontext(Context(prec = 5)), open("out.txt", "w") as out_f:
	out_f.write(f"{one} / {three} = {one / three}\n")
