from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, declarative_base, sessionmaker

Base = declarative_base() # creates a base class

class Band(Base):
    __tablename__ = 'bands' # name of the table to be used by sql alchemy
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    hometown = Column(String, nullable=False)
    
    concerts = relationship("Concert", back_populates="band")
    
    def concerts(self, session):  # this is a method to query concerts 
        return session.query(Concert).filter_by(band_id=self.id).all()
    
    def venues(self, session): #  this is a method to query venues 
        return session.query(Venue).join(Concert).filter(Concert.band_id == self.id).all()
    
    def play_in_venue(self, venue, date, session): # adds  a concert to the band's schedule
        concert = Concert(band_id=self.id, venue_id=venue.id, date=date)
        session.add(concert)
        session.commit()
    
    def all_introductions(self, session):
        return [concert.introduction() for concert in self.concerts(session)]
    
    @classmethod
    def most_performances(cls, session):
        from sqlalchemy import func
        band_performance_counts = session.query(
            cls, func.count(Concert.id).label('performance_count')
        ).join(Concert).group_by(cls.id).order_by(func.count(Concert.id).desc()).first()
        return band_performance_counts[0] if band_performance_counts else None

class Venue(Base):
    __tablename__ = 'venues'
    
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    city = Column(String, nullable=False)
    
    concerts = relationship("Concert", back_populates="venue")
    
    def concerts(self, session):
        return session.query(Concert).filter_by(venue_id=self.id).all()
    
    def bands(self, session):
        return session.query(Band).join(Concert).filter(Concert.venue_id == self.id).all()
    
    def concert_on(self, date, session):
        return session.query(Concert).filter_by(venue_id=self.id, date=date).first()
    
    def most_frequent_band(self, session):
        from sqlalchemy import func
        band_performance_counts = session.query(
            Band, func.count(Concert.id).label('performance_count')
        ).join(Concert).filter(Concert.venue_id == self.id).group_by(Band.id).order_by(func.count(Concert.id).desc()).first()
        return band_performance_counts[0] if band_performance_counts else None

class Concert(Base):
    __tablename__ = 'concerts' #  table names the table for concerts
    
    #names columns in the table
    id = Column(Integer, primary_key=True)
    band_id = Column(Integer, ForeignKey('bands.id'))
    venue_id = Column(Integer, ForeignKey('venues.id'))
    date = Column(String, nullable=False)
    
    band = relationship("Band", back_populates="concerts")
    venue = relationship("Venue", back_populates="concerts")
    
    def band(self):  # returns the band that performed at the concert
        return self.band
    
    def venue(self):   # returns the venue where the concert was held
        return self.venue
    
    def hometown_show(self):   # returns True if the concert was held in the band's hometown
        return self.venue.city == self.band.hometown
    
    def introduction(self):   # returns a string describing the concert
        return f"Hello {self.venue.city}!!!!! We are {self.band.name} and we're from {self.band.hometown}"
