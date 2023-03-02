from fastapi import Depends, HTTPException, status, FastAPI, Response
from models import Note 
from schemas import NoteBaseSchema
from sqlalchemy.orm import Session
from database import get_db
from test_crud import get_items

app = FastAPI()


#  Lister les notes avec fonctions de recherches , pagination et limitation de la requete

@app.get("/items/GET/", response_model=List[NoteBaseSchema])
def read_items(db: Session = Depends(get_db)):
    return get_items(db)

@app.post("/items/POST/")
def test_post_items():
    db = override_get_db() 
    client = TestClient(app)

    client.post("/items/", json={"title": "Item 1"})

    client.post("/items/", json={"title": "Item 2"})

    items = get_items(db)
    assert len(items) == 2