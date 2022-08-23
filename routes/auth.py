from fastapi import APIRouter, Depends
import jwt
from sqlalchemy.orm import Session

from exceptions.ResponseException import ResponseException
from models.auth import Auth
from models.users import Users
from schema.auth import RegisterPostIn, LoginPostIn
from utils.dependencies import get_db, get_password

router = APIRouter()


@router.post('/login')
def login(request: LoginPostIn, db: Session=Depends(get_db), password: str=Depends(get_password)):
    users = db.query(Auth).filter(Auth.email == request.email, Auth.password == password).first()
    if users is not None:
        token = jwt.encode({"email": request.email}, 'aijan', algorithm="HS256")
        return {
            'data': users,
            'status': 'success',
            'token': token
        }
    else:
        raise ResponseException(text='invalid', status=400)


@router.post('/register')
def register(request: RegisterPostIn, db: Session=Depends(get_db), password: str=Depends(get_password)):
    users = db.query(Auth).filter(Auth.email == request.email).first()
    if users is not None:
        raise ResponseException(text='busy', status=401)

    auth = Auth(name=request.name, surname=request.surname, email=request.email, password=password,
                status=request.status)
    db.add(auth)
    token = jwt.encode({"email": request.email}, 'aijan', algorithm="HS256")
    db.commit()

    user = Users(user_id=auth.id)
    db.add(user)
    db.commit()

    db.refresh(user)
    db.refresh(auth)

    return {
        'status': 'success',
        'token': token,
        'auth': auth,
        'user': user
    }
