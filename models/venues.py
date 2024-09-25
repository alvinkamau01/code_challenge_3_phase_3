from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from .base import Base

class Venue(Base):
    __tablename__ = 'venues'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    city = Column(String)

    concerts = relationship("Concert", back_populates="venue")



    def __init__(self,name,city):
        self.name = name
        self.city = city




    def  __repr__(self):
        return f"Venue('{self.name}', '{self.city}')"
    

    def get_concerts(self): ## Returns a collection of all concerts for the Venue
        return self.concerts

    def get_bands(self, session):## Returns a collection of all bands who performed at the Venue
        from models.bands import Band
        from models.concerts import Concert 
        return session.query(Band).join(Concert).filter(Concert.venue_id == self.id).all()
