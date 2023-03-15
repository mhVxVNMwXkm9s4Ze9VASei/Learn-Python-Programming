# oop/simplest.class.py
class Simplest(): # when empty, the braces are optional
	pass

print(type(Simplest)) # what type is this? object
simp = Simplest() # we create an instance of Simplest: simp
print(type(simp)) # what type is simp?
# is simp an instance of Simplest?
print(type(simp) is Simplest) # there's a better way to do this
