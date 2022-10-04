from sqlalchemy import Column, Integer, String, Text, TIMESTAMP

from utils.database import Base


class News(Base):
    __tablename__ = 'news_product'

    title = Column(String, nullable=False)
    date = Column(TIMESTAMP, nullable=False)
    text = Column(Text, nullable=False)
    img = Column(String, nullable=False)

