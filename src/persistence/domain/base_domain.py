from sqlalchemy import Column, Boolean, Integer
from sqlalchemy.ext.declarative import as_declarative
from sqlalchemy.ext.declarative.base import declared_attr


@as_declarative()
class BaseDomain:
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    available = Column(Boolean, default=False, nullable=False, index=True)

    @declared_attr
    def __tablename__(self) -> str:
        return self.__name__.lower()

    @declared_attr
    def __table_args__(self) -> dict:
        return {'schema': ''}

    @property
    def available(self) -> bool: return self.available    

    FIELDS = {
        'id': int,
        'available': bool
    }
