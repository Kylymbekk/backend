from sqlalchemy import Column, String, Text, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from utils.database import Base


class Contacts(Base):
    __tablename__ = 'Contacts'

    type = Column(String(55), nullable=False)
    value = Column(Text, nullable=False)
    start_at = Column(DateTime, nullable=True)
    end_at = Column(DateTime, nullable=True)
    auth_id = Column(Integer, ForeignKey('auth.id'), nullable= False)

    auth = relationship('Auth')
