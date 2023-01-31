from sqlalchemy.orm import Session
from sqlalchemy.orm.exc import NoResultFound
from models import Link


def shorten_link(db: Session, url: str, base_url: str) -> Link:
    while "\\" in url:
        url = url.replace("\\", '/')
    if Link.check_if_url_exists(db, url):
        return db.query(Link).filter(Link.url == url).first()
    short_url = Link.get_short_url(db, base_url)
    new_link = Link(
        url=url,
        short_url=short_url
    )
    db.add(new_link)
    db.commit()
    return new_link


def get_full_link(db: Session, link: str, base_url: str):
    short_url = f"{base_url}{link}"
    try:
        return db.query(Link).filter(Link.short_url == short_url).first()
    except Exception as e:
        print(db.query(Link).filter(Link.short_url == short_url).first())
        return e # 404