# oop/class.attribute.shadowing.py
class Point:
	x = 10
	y = 7

p = Point()
print(p.x) # 10 (from class attribute)
print(p.y) # 7 (from class attribute)

p.x = 12 # p gets its own 'x' attribute
print(p.x) # 12 (now found on the instance)
print(Point.x) # 10 (class attribute still the same)

del p.x # we delete the instance attribute
print(p.x) # 10 (now search has to go again to find the class attribute)

p.z = 3 # Let's make it a 3D point
print(p.z) # 3

print(Point.z)
# AttributeError: type object 'Point' has no attribute 'z'
