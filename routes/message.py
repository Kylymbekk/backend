from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from exceptions.ResponseException import ResponseException
from models import Message
from models.auth import Auth
from utils.dependencies import get_db, get_auth

router = APIRouter()


@router.get('/get')
def massage_get(auth: Auth=Depends(get_auth), db: Session=Depends(get_db)):
    if auth is None:
        ResponseException(text='dont message error', status=400)

    message = db.query(Message).all()

    return {
        'status': 'success',
        'message': message,
    }