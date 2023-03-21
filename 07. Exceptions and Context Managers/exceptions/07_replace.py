# exceptions/replace.py
class NotFoundError(Exception):
	pass

vowels = {
	'a': 1,
	'e': 5,
	'i': 9,
	'o': 15,
	'u': 21
}

try:
	pos = vowels['y']
except KeyError as e:
	raise NotFoundError(*e.args) from e
