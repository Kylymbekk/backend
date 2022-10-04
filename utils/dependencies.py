import random
from time import time

from fastapi import Body, Header, Depends, UploadFile, Form
from sqlalchemy.orm import Session

from models import Auth, Users
from utils.database import SessionLocal
import jwt
import hashlib


async def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


async def get_user(db: Session = Depends(get_db), authorization: str = Header()):
    token = jwt.decode(authorization[7:], 'aijan', algorithms=["HS256"])
    auth = db.query(Auth).filter(Auth.email == token['email']).first()
    if auth is None:
        return None
    return db.query(Users).filter(auth.id == Users.user_id).first()


async def get_auth(db: Session = Depends(get_db), authorization: str = Header()):
   token = jwt.decode(authorization[7:], 'aijan', algorithms=["HS256"])
   return db.query(Auth).filter(token['email'] == Auth.email).first()


async def get_auth_argument(token: str, db: Session = Depends(get_db)):
   token = jwt.decode(token, 'aijan', algorithms=["HS256"])
   print(token)
   return db.query(Auth).filter(token['email'] == Auth.email).first()


async def get_password(password: str = Body()):
    password = hashlib.md5(password.encode('utf-8')).hexdigest()
    return password


async def get_image_name(image: UploadFile = Form()):
    image_name = hashlib.md5((image.filename + str(time()) + str(random.randint(1, 1000000))).encode('utf-8')).hexdigest()
    return image_name + '.' + image.filename.split('.')[-1]


async def upload_image(image: UploadFile = Form()):
    pass

