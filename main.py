from fastapi import Depends, HTTPException, status, FastAPI, Response
from models import Note 
from schemas import NoteBaseSchema
from sqlalchemy.orm import Session
from database import get_db

app = FastAPI()


#  Lister les notes avec fonctions de recherches , pagination et limitation de la requete
@app.get('/items/GET/')
def get_notes(db: Session = Depends(get_db), limit: int = 10, page: int = 1, search: str = ''):
    skip = (page - 1) * limit

    notes = db.query(Note).filter(
        Note.titre.contains(search)).limit(limit).offset(skip).all()
    
    return {'status': 'success', 'results': len(notes), 'notes': notes}


# creer une note
@app.post('/items/POST/', status_code=status.HTTP_201_CREATED)
def create_note(payload: NoteBaseSchema, db: Session = Depends(get_db)):
    new_note = Note(**payload.dict())
    db.add(new_note)
    db.commit()
    db.refresh(new_note)
    return {"status": "success", "note": new_note}


# modifier une note avec son id
@app.patch('/items/MODIFY/{noteId}')
def update_note(noteId: str, payload: NoteBaseSchema, db: Session = Depends(get_db)):
    note_query = db.query(Note).filter(Note.id == noteId)
    db_note = note_query.first()

    if not db_note:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Aucune note avec l id {noteId} a été retrouvé')
    
    update_data = payload.dict(exclude_unset=True)
    note_query.filter(Note.id == noteId).update(update_data,synchronize_session=False)
    db.commit()
    db.refresh(db_note)
    return {"status": "success", "note": db_note}



# supprimer une note avec son id
@app.delete('/items/DELETE/{noteId}')
def delete_post(noteId: str, db: Session = Depends(get_db)):
    note_query = db.query(Note).filter(Note.id == noteId)
    note = note_query.first()
    if not note:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Aucune note avec l id {noteId} a été retrouvé')
    
    note_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


# retrouver une note avec son id
@app.get('/items/GET/{noteId}')
def get_post(noteId: str, db: Session = Depends(get_db)):
    note = db.query(Note).filter(Note.id == noteId).first()
    if not note:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Aucune note avec l id {noteId} a été retrouvé')

    return {"status": "success", "note": note}