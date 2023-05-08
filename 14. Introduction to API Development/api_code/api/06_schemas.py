# api_code/api/schemas.py
from pydantic import BaseModel

class StationBase(BaseModel):
	code: str
	country: str
	city: str

class Station(StationBase):
	id: int
	class Config:
		orm_mode = True

class StationCreate(StationBase):
	pass
