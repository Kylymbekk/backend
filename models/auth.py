from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship

from utils.database import Base


class Auth(Base):
    __tablename__ = "auth"

    name = Column(String(55), nullable=False)
    surname = Column(String(55), nullable=False)
    email = Column(String(55), nullable=False)
    password = Column(String(32), nullable=False)
    status = Column(Text)

    # receives = relationship('History', back_populates='receiver')
    contacts = relationship('Contacts', back_populates='auth')
    messages = relationship('Message', back_populates='sender')

