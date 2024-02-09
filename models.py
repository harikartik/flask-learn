from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class UrlRepo(Base):
    __tablename__ = 'urls'

    id = Column(Integer, primary_key=True)
    url = Column(String(250), nullable=False, unique=True)
    target = Column(Integer, default=0)
    timestamp = Column(DateTime, default=datetime.utcnow)
