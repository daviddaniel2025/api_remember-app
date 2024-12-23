from sqlalchemy import Column, Integer, String, Date
from database import Base


class Note(Base):
    __tablename__ = "notes"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)  # Limite de 255 caracteres
    description = Column(String(1000), nullable=False)  # Limite de 1000 caracteres
    event_date = Column(Date, nullable=False)