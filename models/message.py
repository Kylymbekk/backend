from sqlalchemy import Column, Integer, Text, TIMESTAMP, ForeignKey
from sqlalchemy.orm import relationship

from utils.database import Base


class Message(Base):
    __tablename__ = 'message'

    receiver_id = Column(Integer)
    sender_id = Column(Integer, ForeignKey('auth.id'))
    text = Column(Text)
    date = Column(TIMESTAMP)

    sender = relationship('Auth')





