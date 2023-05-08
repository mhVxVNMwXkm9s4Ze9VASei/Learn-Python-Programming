# api_code/api/stations.py
from typing import Optional
from FastAPI import (
	APIRouter,
	Depends,
	HTTPException,
	Response,
	status
)
from sqlalchemy.orm import Session
from . import crud
from .deps import get_db
from .schemas import (
	Station,
	StationCreate,
	StationUpdate,
	Train
)

router = APIRouter(prefix = "/stations")

@router.get("", response_model = list[Station], tags = ["Stations"])
def get_stations(
	db: Session = Depends(get_db),
	code: Optional[str] = None
):
	return crud.get_stations(db = db, code = code)

@router.get(
	"/{station_id}",
	response_model = Station,
	tags = ["Stations"]
)
def get_station(station_id: int, db: Session = Depends(get_db)):
	db_station = crud.get_station(db = db, station_id = station_id)
	if db_station is None:
		raise HTTPException(
			status_code = 404,
			detail = f"Station {station_id} not found.",
		)
	return db_station

@router.post(
	"",
	response_model = Station,
	status_code = status.HTTP_201_CREATED,
	tags = ["Stations"],
)
def create_station(
	station: StationCreate,
	db: Session = Depends(get_db)
):
	db_station = crud.get_station_by_code(
		db = db,
		code = station.code
	)
	if db_station:
		raise HTTPException(
			status_code = 400,
			detail = f"Station {station.code} already exists.",
		)
	return crud.create(db = db, station = station)
