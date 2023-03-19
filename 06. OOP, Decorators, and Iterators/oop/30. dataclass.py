# oop/dataclass.py
from dataclasses import dataclass

@dataclass
class Body:
	'''Class to represent a physical body.'''
	name: str
	mass: float = 0 # Kg
	speed: float = 1. # m/s

	def kinetic_energy(self) -> float:
		return (self.mass * self.speed * self.speed) / 2

body = Body('Ball', 19, 3.1415)
print(body.kinetic_energy()) # 93.755711375 Joules
print(body) # Body(name = 'Ball', mass = 19, speed = 3.1415)
