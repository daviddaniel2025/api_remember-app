from pydantic import BaseModel
from datetime import date

class NoteBase(BaseModel):
    title: str
    description: str
    event_date: date

class NoteCreate(NoteBase):
    pass

class NoteUpdate(NoteBase):
    pass

class Note(NoteBase):
    id: int

    class Config:
        from_attributes = True