# walrus.if.py
# without walrus operator
remainder = value % modulus
if remainder:
	print(f"Not divisible! The remainder is {remainder}.")

# with walrus operator
if remainder := value % modulus:
	print(f"Not divisible! The remainder is {remainder}.")