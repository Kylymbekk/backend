from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import jwt

from exceptions.ResponseException import ResponseException
from models.auth import Auth
from models.users import Users
from schema.transfer import TransferPost
from utils.dependencies import get_db, get_token

router = APIRouter()


@router.post('')
def transfer(request: TransferPost, db: Session=Depends(get_db), token: dict=Depends(get_token)):
    user = db.query(Auth).filter(Auth.email == token['email']).first()
    user = db.query(Users).filter(user.id == Users.user_id).first()
    receiver = db.query(Auth).filter(Auth.email == request.email).first()
    receiver = db.query(Users).filter(Users.user_id == receiver.id).first()

    balance = request.balance + ((request.balance / 100) * 5)

    if user.balance < balance:
        raise ResponseException(text='not enov fands', status=400)
    if token['email'] == request.email:
        raise ResponseException(text='dont your your', status=400)
    user.balance -= balance
    receiver.balance += request.balance
    db.commit()

    return f'transfer {user.balance}'


@router.post('/get_balance')
def get_balance(request: TransferPost, db: Session=Depends(get_db), token: dict=Depends(get_token)):
    user = db.query(Auth).filter(Auth.email == token['email']).first()
    user = db.query(Users).filter(user.id == Users.user_id).first()
    receiver = db.query(Auth).filter(Auth.email == request.email).first()
    receiver = db.query(Users).filter(Users.user_id == receiver.id).first()
    receiver.balance += request.balance
    db.commit()

    return f'transfer {user.balance}'





