# sum.example.2.py
s = sum([n * n for n in range(10 ** 9)]) # this is killed
# s = sum(n * n for n in range(10 ** 9)) # this succeeds
print(s)
