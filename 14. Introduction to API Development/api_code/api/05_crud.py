# api_code/api/crud.py
from datetime import datetime, timezone
from sqlalchemy import delete, update
from sqlalchemy.orm import Session, aliased
from . import models, schemas

def get_stations(db: Session, code: str = None):
	q = db.query(models.Station)
	if code is not None:
		q = q.filter(models.Station.code.ilike(code))
	return q.all()

def get_station_by_code(db: Session, code: str):
	return (
		db.query(models.Station)
			.filter(models.Station.code.ilike(code))
			.first()
	)

def create_station(
	db: Session,
	station: schemas.StationCreate,
):
	db_station = models.Station(**station.dict())
	db.add(db_station)
	db.commit()
	db.refresh(db_station)
	return db_station

def update_station(
		db: Session,
		station: schemas.StationUpdate,
		station_id: int
):
	stm = (
		update(models.Station)
			.where(models.Station.id == station_id)
			.values(station.dict(exclude_unset = True))
	)
	result = db.execute(stm)
	db.commit()
	return result.rowcount

def delete_station(db: Session, station_id: int):
	stm = delete(models.Station).where(
		models.Station.id == station_id
	)
	result = db.execute(stm)
	db.commit()
	return result.rowcount
