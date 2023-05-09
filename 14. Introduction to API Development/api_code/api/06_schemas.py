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

from typing import Optional
class StationUpdate(StationBase):
	code: Optional[str] = None
	country: Optional[str] = None
	city: Optional[str] = None

class Auth(BaseModel):
	email: str
	password: str
