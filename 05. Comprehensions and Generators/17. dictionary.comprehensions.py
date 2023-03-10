# dictionary.comprehensions.py
from string import ascii_lowercase
lettermap = {c: k for k, c in enumerate(ascii_lowercase, 1)}
print(lettermap)

lettermap = dict((c, k) for k, c in enumerate(ascii_lowercase, 1))
print(lettermap)
