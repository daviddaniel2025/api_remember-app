from repositories.noteRepository import NoteRepository
from sqlalchemy.orm import Session
from schemas import NoteCreate, NoteUpdate
from fastapi import HTTPException

class NoteService:
    def __init__(self, db: Session):
        self.repository = NoteRepository(db)

    def list_notes(self):
        return self.repository.get_all()

    def create_note(self, note: NoteCreate):
        return self.repository.create(note)

    def update_note(self, note_id: int, note: NoteUpdate):
        db_note = self.repository.get_by_id(note_id)
        if not db_note:
            raise HTTPException(status_code=404, detail="Nota não encontrada")
        return self.repository.update(note_id, note)

    def delete_note(self, note_id: int):
        db_note = self.repository.get_by_id(note_id)
        if not db_note:
            raise HTTPException(status_code=404, detail="Nota não encontrada")
        self.repository.delete(note_id)
        return {"message": "Nota deletada com sucesso"}