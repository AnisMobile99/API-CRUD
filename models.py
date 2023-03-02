from database import Base
from sqlalchemy import TIMESTAMP, Column, String, Integer
from sqlalchemy.sql import func


class Note(Base):
    __tablename__ = 'notes'
    id = Column(Integer, primary_key=True)
    titre = Column(String, nullable=False)
    description = Column(String, nullable=False)


