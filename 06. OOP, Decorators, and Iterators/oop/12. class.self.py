# oop/class.self.py
class Square:
	side = 8
	def area(self): # self is a reference to an instance
		return self.side * self.side

sq = Square()
print(sq.area()) # 64 (side is found on the class)
print(Square.area(sq)) # 64 (equivalent to sq.area())

sq.side = 10
print(sq.area()) # 100 (side is found on the instance)
