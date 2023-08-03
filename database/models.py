from sqlalchemy import Column, DateTime, String, Integer, ForeignKey, Float, Date, Boolean, BigInteger, null
from sqlalchemy.orm import relationship
from database import Base


class Cars(Base):
    __tablename__ = 'cars'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    model = Column(String, nullable=False)
    year = Column(String, nullable=False)