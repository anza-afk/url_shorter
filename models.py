from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Session
from string import ascii_letters, digits
from random import choices

from db import Base

class Link(Base):
    __tablename__ = "__links__"

    id = Column(Integer, primary_key=True, index=True)
    url = Column(String, index=True)
    short_url = Column(String, index=True)
    
    @staticmethod
    def check_if_url_exists(db: Session, url: str, long: bool=True):
        query = db.query(Link).filter(
            Link.url == url).first() if long else db.query(Link).filter(
                Link.short_url == url).first()
        return query

    @staticmethod
    def get_short_url(db: Session, BASE_URL: str):
        symbols = ascii_letters+digits
        while True:
            url = f"{BASE_URL}{''.join((choices(symbols, k=6)))}"
            if not Link.check_if_url_exists(db, url, long=False):
                break
        return url
