from fastapi import APIRouter, Depends
import jwt
from sqlalchemy.orm import Session

from models import SessionLocal
from models.auth import Auth
from models.users import Users
from utils.dependencies import get_db

router = APIRouter()

session = SessionLocal()


@router.get('/get')
def users(token: str, db: Session=Depends(get_db)):
    token = jwt.decode(token, 'aijan', algorithms=["HS256"])
    auth = db.query(Auth).filter(token['email'] == Auth.email).first()
    user = db.query(Users).filter(Users.user_id == auth.id).first()

    return {
        'data': user,
        'status': 'success'
    }
