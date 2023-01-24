from sqlalchemy.orm import Session
from sqlalchemy.orm.exc import NoResultFound
import schemas
from models import Link

BASE_URL = "HTTP://TEST0.RU"

def shorten_link(db: Session, link: str):
    if Link.check_if_url_exists(link):
        return db.query(Link).get(Link.link == link)     
    short_link = Link.get_short_url(BASE_URL)
    new_link = Link(
        link=link,
        short_link=short_link
    )
    db.add(new_link)
    db.commit()
    return new_link


def get_full_link(db: Session, link: str):
    try:
        return db.query(Link).get(Link.short_link == link) 
    except NoResultFound as e:
        return e # 404