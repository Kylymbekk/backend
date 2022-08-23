from sqlalchemy import Column, Integer, String, Text

from models import Base


class Auth(Base):
    __tablename__ = "auth"

    id = Column(Integer, primary_key=True, unique=True)
    name = Column(String(55), nullable=False)
    surname = Column(String(55), nullable=False)
    email = Column(String(55), nullable=False)
    password = Column(String(32), nullable=False)
    status = Column(Text)

