from fastapi import Body

from models import SessionLocal
import jwt
import hashlib


async def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


async def get_token(token: str = Body()):
    token = jwt.decode(token, 'aijan', algorithms=["HS256"])
    return token


async def get_password(password: str = Body()):
    password = hashlib.md5(password.encode('utf-8')).hexdigest()
    return password
