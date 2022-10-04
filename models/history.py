from sqlalchemy import Column, Integer, ForeignKey, Float
from sqlalchemy.orm import relationship

from utils.database import Base


class History(Base):
    __tablename__ = 'history'



    receiver_id = Column(Integer, ForeignKey('auth.id'), nullable=True)
    sender_id = Column(Integer, ForeignKey('auth.id'), nullable=True)
    price = Column(Float, nullable=True)
    commission = Column(Float, nullable=True)

    receiver = relationship('Auth', foreign_keys=[receiver_id])
    sender = relationship('Auth', foreign_keys=[sender_id])
