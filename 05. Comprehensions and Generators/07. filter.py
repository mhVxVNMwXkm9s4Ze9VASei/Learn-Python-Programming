# filter.py
test = [2, 5, 8, 0, 0, 1, 0]
print(list(filter(None, test)))
print(list(filter(lambda x: x, test))) # equivalent to the previous one
print(list(filter(lambda x: x > 4, test))) # keep only items > 4