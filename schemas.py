from pydantic import BaseModel

class LinkBase(BaseModel):
    url: str
    
    class Config:
        orm_mode = True

class LinkCreate(LinkBase):
    pass


class Link(LinkBase):
    id: int
    short_url: str
