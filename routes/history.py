from fastapi import APIRouter, Depends
from sqlalchemy import or_
from sqlalchemy.orm import Session

from exceptions.ResponseException import ResponseException
from models import Auth, History
from utils.dependencies import get_db, get_auth

router = APIRouter()


@router.get('/get')
def history(db: Session = Depends(get_db), auth: Auth = Depends(get_auth)):
    if auth is None:
        raise ResponseException(text='dont history', status=400)

    history = db.query(History).filter(or_(auth.id == History.receiver_id, auth.id == History.sender_id)).all()

    return {
        'status': 'success',
        'history': history
    }
