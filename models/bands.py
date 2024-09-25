from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from .base import  Base

class Band(Base):
    __tablename__ = 'bands'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    hometown = Column(String)
    concerts = relationship("Concert", back_populates="band")

    def __init__(self,name,hometown):
        self.name = name
        self.hometown = hometown

    def  __repr__(self):
        return f"Band('{self.name}', '{self.hometown}')"

    def get_concerts(self): ## Returns a collection of all concerts that the Band has played
        return self.concerts

    def get_venues(self, session): ## Returns a collection of all venues where the Band has performed
        from models.venues import Venue
        from models.concerts import Concert
        return session.query(Venue).join(Concert).filter(Concert.band_id == self.id).all()
    