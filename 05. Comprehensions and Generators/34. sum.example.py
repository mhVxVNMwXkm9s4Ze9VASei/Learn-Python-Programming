# sum.example.py
s1 = sum([n * n for n in range(10 ** 6)]) # list comprehension
s2 = sum((n * n for n in range(10 ** 6))) # generator expression
s3 = sum(n * n for n in range(10 ** 6)) # normal function?

print(s1)
print(s2)
print(s3)
