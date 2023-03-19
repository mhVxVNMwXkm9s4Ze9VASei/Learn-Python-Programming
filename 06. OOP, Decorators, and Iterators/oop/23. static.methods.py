# oop/static.methods.py
class StringUtil:

	@staticmethod
	def is_palindrome(s, case_insensitive = True):
		# we only allow letters and numbers
		s = ''.join(c for c in s if c.isalnum()) # Study this!
		# For case-insensitive comparison, we make s lowercase
		if case_insensitive:
			s = s.lower()
		for c in range(len(s) // 2):
			if s[c] != s[-c - 1]:
				return False
		return True

	@staticmethod
	def get_unique_words(sentence):
		return set(sentence.split())

print(
	StringUtil.is_palindrome(
		'Radar',
		case_insensitive = False
	)
) # False: case sensitive
print(StringUtil.is_palindrome('A nut for a jar of tuna')) # True
print(StringUtil.is_palindrome('Never odd, Or Even!')) # True
print(
	StringUtil.is_palindrome(
		'In Girum Imus Nocte Et Consumimur Igni' # Latin! Show-off!!
	)
) # True
print(
	StringUtil.get_unique_words(
		'I love palindromes. I really love them!'
	)
) # { 'them!', 'palindromes.', 'I', 'really', 'love' }
