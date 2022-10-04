from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from exceptions.ResponseException import ResponseException
from models import History
from models.auth import Auth
from models.users import Users
from schema.transfer import TransferPost
from utils.dependencies import get_db, get_user, get_auth

router = APIRouter()


@router.post('')
def transfer(request: TransferPost, db: Session=Depends(get_db), user: Users=Depends(get_user), auth: Auth=Depends(get_auth)):
    receiver1 = db.query(Auth).filter(Auth.email == request.email).first()

    if receiver1 is None:
        raise ResponseException(text='dont your account', status=400)

    receiver2 = db.query(Users).filter(Users.user_id == receiver1.id).first()

    commission = (request.balance / 100) * 5
    balance = request.balance + commission

    if user.balance < balance:
        raise ResponseException(text='not enov fands', status=400)
    if auth.email == request.email:
        raise ResponseException(text='dont your your', status=400)
    user.balance -= balance
    receiver2.balance += request.balance

    history = History(receiver_id=receiver2.id, sender_id=auth.id, price=request.balance, commission=commission)
    db.add(history)

    db.commit()

    return f'transfer {user.balance}'


@router.post('/get_balance')
def get_balance(request: TransferPost, db: Session=Depends(get_db), auth: Auth=Depends(get_auth)):
    receiver1 = db.query(Auth).filter(Auth.email == request.email).first()
    receiver2 = db.query(Users).filter(Users.user_id == receiver1.id).first()
    receiver2.balance += request.balance
    commission = (request.balance / 100) * 5

    history = History(receiver_id=receiver1.id, sender_id=auth.id, price=request.balance, commission=commission)
    db.add(history)

    db.commit()

    return f'transfer {receiver2.balance}'





