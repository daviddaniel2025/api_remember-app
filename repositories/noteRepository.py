from sqlalchemy.orm import Session
from models import Note
from schemas import NoteCreate, NoteUpdate

class NoteRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return self.db.query(Note).all()

    def get_by_id(self, note_id: int):
        return self.db.query(Note).filter(Note.id == note_id).first()

    def create(self, note: NoteCreate):
        db_note = Note(**note.dict())
        self.db.add(db_note)
        self.db.commit()
        self.db.refresh(db_note)
        return db_note

    def update(self, note_id: int, note: NoteUpdate):
        db_note = self.get_by_id(note_id)
        if db_note:
            for key, value in note.dict().items():
                setattr(db_note, key, value)
            self.db.commit()
            self.db.refresh(db_note)
        return db_note

    def delete(self, note_id: int):
        db_note = self.get_by_id(note_id)
        if db_note:
            self.db.delete(db_note)
            self.db.commit()
        return db_note