from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship, declarative_base
from .base import Base

class Concert(Base):
    __tablename__ = 'concerts'
    id = Column(Integer, primary_key=True, autoincrement=True)
    band_id = Column(Integer, ForeignKey('bands.id'))
    venue_id = Column(Integer, ForeignKey('venues.id'))
    date = Column(Integer)
    band = relationship("Band", back_populates="concerts")
    venue = relationship("Venue", back_populates="concerts")


    def __init__(self,band_id,venue_id,date):
        self.band_id = band_id
        self.venue_id = venue_id
        self.date = date
        


    def  __repr__(self):
        return f"Concert(id={self.id}, band_id={self.band_id}  venue_id={self.venue_id}, date={self.date})"



    def get_band(self):##Returns the Band instance for this Concert
        return self.band

    def get_venue(self):##Returns the Venue instance for this Concert
        return self.venue

