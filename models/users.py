from sqlalchemy import Column, Integer, Text

from utils.database import Base


class Users(Base):
    __tablename__ = "users"

    balance = Column(Integer, default='100')
    img = Column(Text)
    user_id = Column(Integer, nullable=False)
