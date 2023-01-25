from fastapi import Depends, FastAPI, status, Path, Request
from sqlalchemy.orm import Session

import crud, models, schemas
from config import settings
from db import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
base_url = settings.base_url


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/shorten/", response_model=schemas.Link, status_code=status.HTTP_201_CREATED)
async def get_short_url(
    url: schemas.LinkCreate,
    db: Session = Depends(get_db)):
    short_link = crud.shorten_link(db, url.url, base_url)
    return short_link


@app.get("/{short_link}", response_model=schemas.Link, status_code=status.HTTP_200_OK)
async def get_full_url(
    short_link: str = Path(min_length=6, max_length=6),
    db: Session = Depends(get_db)
):
    full_link = crud.get_full_link(db, short_link, base_url)
    return full_link
