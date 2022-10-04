import sqlalchemy
from sqlalchemy import Column, Integer
from sqlalchemy.ext.declarative import declarative_base, DeclarativeMeta
from sqlalchemy.orm import sessionmaker


def orm_to_json(orm):
    if isinstance(orm, dict):
        return orm
    elif isinstance(orm, list):
        return [
            i.to_dict('bulk') for i in orm
        ]
    elif isinstance(orm.__class__, DeclarativeMeta):
        return orm.to_dict('item')


class BaseModel(object):
    id = Column(Integer, primary_key=True, index=True)

    _item_response = []
    _bulk_response = []

    def to_dict(self, t):
        fields = ['id'] + (self._item_response if t == 'item' else self._bulk_response)
        return {c: orm_to_json(getattr(self, c)) for c in fields}


engine = sqlalchemy.create_engine("postgresql://abcde:postgres@localhost:5432/Mega-Beeline")
SessionLocal = sessionmaker(bind=engine)
session = SessionLocal()
Base = declarative_base(cls=BaseModel)
