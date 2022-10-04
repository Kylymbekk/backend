from sqlalchemy import Column, Integer, String, TIMESTAMP

from utils.database import Base


class Change(Base):
    __tablename__ = "change"

    date = Column(TIMESTAMP)
    amount = Column(Integer)
    from_currency = Column(String(10))
    to_currency = Column(String(10))
    result_amount = Column(Integer)
