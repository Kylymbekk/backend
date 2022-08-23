from sqlalchemy import Column, Integer, String, Text, Date

from models import Base


class News(Base):
    __tablename__ = 'news_product'

    id = Column(Integer, primary_key=True, unique=True)
    title = Column(String, nullable=False)
    date = Column(Date, nullable=False)
    text = Column(Text, nullable=False)
    img = Column(String, nullable=False)

