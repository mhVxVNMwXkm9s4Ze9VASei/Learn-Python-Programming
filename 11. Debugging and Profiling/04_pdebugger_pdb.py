# pdebugger_pdb.py
# d comes from a JSON payload we don't control XD!
d = {'first': 'v1', 'second': 'v2', 'fourth': 'v4'}

#keys also comes from a JSON payload we don't control XD!
keys = ('first', 'second', 'third', 'fourth')
def do_something_with_value(value):
	print(value)

breakpoint()

for key in keys:
	do_something_with_value(d[key])

print('Validation done.')
