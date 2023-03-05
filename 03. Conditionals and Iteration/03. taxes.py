# taxes.py
income = 15_000
if income < 10_000:
	tax_coefficient = 0.0
elif income < 30_000:
	tax_coefficient = 0.2
elif income < 100_000:
	tax_coefficient = 0.35
else:
	tax_coefficient = 0.45

print(f'You will pay: ${income * tax_coefficient} in taxes!')