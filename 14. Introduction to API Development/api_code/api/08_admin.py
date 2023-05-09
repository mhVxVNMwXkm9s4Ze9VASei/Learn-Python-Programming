# api_code/api/admin.py
from .util import is_admin

router = APIRouter(prefix = "/main")

def ensure_admin(
    settings: Settings,
    authorization: str
):
	if not is_admin(
		settings = settings, authorization = authorization
	):
		raise HTTPException(
			status_code = status.HTTP_401_UNAUTHORIZED,
			detail = f"You must be an admin to access this endpoint."
		)

@router.delete("/stations/{station_id}", tags = ["Admin"])
def admin_delete_station(
	station_id: int,
	authorization: Optional[str] = Header(None),
	settings: Settings = Depends(get_settings),
	db: Session = Depends(get_db),
):
	ensure_admin(settings, authorization)
	row_count = crud.delete_station(db = db, station_id = station_id)
	if row_count:
		return Response(status_code = status.HTTP_204_NO_CONTENT)
	return Response(status_code = status.HTTP_404_NOT_FOUND)
