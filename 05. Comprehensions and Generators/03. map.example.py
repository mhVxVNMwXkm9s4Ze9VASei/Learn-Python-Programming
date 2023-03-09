# map.example.py
print(map(lambda *a: a, range(3))) # 1 iterable

print(list(map(lambda *a: a, range(3)))) # 1 iterable

print(list(map(lambda *a: a, range(3), 'abc'))) # 2 iterables

print(list(map(lambda *a: a, range(3), 'abc', range(4, 7)))) # 3

# map stops at the shortest iterator
print(list(map(lambda *a: a, (), 'abc'))) # empty tuple is shortest

print(list(map(lambda *a: a, (1, 2), 'abc'))) # (1, 2) shortest

print(list(map(lambda *a: a, (1, 2, 3, 4), 'abc'))) # 'abc' shortest
