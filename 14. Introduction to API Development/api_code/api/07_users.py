# api_code/api/users.py
from .util import InvalidToken, create_token, extract_payload

@router.post("/authenticate", tags = ["Auth"])
def authenticate(
	auth: Auth,
	db: Session = Depends(get_db),
	settings: Settings = Depends(get_settings),
):
	db_user = crud.get_user_by_email(db = db, email = auth.email)
	if db_user is None:
		raise HTTPException(
			status_code = status.HTTP_404_NOT_FOUND,
			detail = f"User {auth.email} not found.",
		)
	
	if not db_user.is_valid_password(auth.password):
		raise HTTPException(
			status_code = status.HTTP_401_UNAUTHORIZED,
			detail = "Wrong username/password.",
		)

	payload = {
		"email": auth.email,
		"role": db_user.role_value,
	}
	return create_token(payload, settings.secret_key)
