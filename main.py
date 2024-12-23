from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, engine
import models
from schemas import NoteCreate, NoteUpdate
from services.noteService import NoteService
from fastapi.middleware.cors import CORSMiddleware

# Criar as tabelas no banco de dados
models.Base.metadata.create_all(bind=engine)

app = FastAPI()



# Dependência para obter a conexão do banco de dados
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Inicializa o serviço de notas
def get_note_service(db: Session = Depends(get_db)):
    return NoteService(db)

# Lista todas a notas
@app.get("/notes")
def list_notes(service: NoteService = Depends(get_note_service)):
    return service.list_notes()

# Salva uma nota no banco de dados
@app.post("/notes")
def create_note(note: NoteCreate, service: NoteService = Depends(get_note_service)):
    return service.create_note(note)

# Editar informação de uma nota por Id
@app.put("/notes/{id}")
def update_note(id: int, note: NoteUpdate, service: NoteService = Depends(get_note_service)):
    return service.update_note(id, note)

# Deleta informação de uma nota  por Id
@app.delete("/notes/{id}")
def delete_note(id: int, service: NoteService = Depends(get_note_service)):
    return service.delete_note(id)