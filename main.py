from fastapi import Depends, FastAPI, status, Body, HTTPException
from sqlalchemy.orm import Session

import crud, models, schemas
from db import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/shorten/", response_model=schemas.Link, status_code=status.HTTP_201_CREATED)
async def get_short_url(long_link: str, db: Session = Depends(get_db)):
    short_link = crud.shorten_link(db, long_link)
    return short_link


@app.get("/shorten/", response_model=schemas.Link, status_code=status.HTTP_200_OK)
async def get_full_url(short_link:str, db: Session = Depends(get_db)):
    full_link = crud.get_full_link(db, short_link)
    return full_link
