from fastapi import APIRouter, Depends
import jwt
from sqlalchemy.orm import Session

from exceptions.ResponseException import ResponseException
from models.auth import Auth
from models.news import News
from utils.dependencies import get_db

router = APIRouter()


@router.get('/get')
def news(token: str, db: Session=Depends(get_db)):
    token = jwt.decode(token, 'aijan', algorithms=["HS256"])
    user = db.query(Auth).filter(Auth.email == token['email']).first()
    if user is not None:
        new = db.query(News).limit(100).all()

        return {
            'data': new
        }
    else:
        raise ResponseException(text='invalid token', status=400)
