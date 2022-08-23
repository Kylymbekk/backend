from sqlalchemy import Column, Integer, Text

from models import Base


class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    balance = Column(Integer, default='100')
    img = Column(Text)
    user_id = Column(Integer, nullable=False)
