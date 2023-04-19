# assertions.py
mylist = [1, 2, 3] # pretend this comes from an external source
assert 4 == len(mylist), f'Mylist has {len(mylist)} elements' # this will break
for position in range(4):
	print(mylist[position])
