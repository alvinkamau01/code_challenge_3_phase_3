import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Band, Venue, Concert

@pytest.fixture(scope='module')
def setup_database():
    engine = create_engine('sqlite:///test_concerts.db')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    yield session
    Base.metadata.drop_all(engine)

def test_band_creation(setup_database):
    session = setup_database
    band = Band(name='The Rockers', hometown='New York')
    session.add(band)
    session.commit()
    retrieved_band = session.query(Band).filter_by(name='The Rockers').first()
    assert retrieved_band is not None
    assert retrieved_band.hometown == 'New York'

def test_venue_creation(setup_database):
    session = setup_database
    venue = Venue(title='Madison Square Garden', city='New York')
    session.add(venue)
    session.commit()
    retrieved_venue = session.query(Venue).filter_by(title='Madison Square Garden').first()
    assert retrieved_venue is not None
    assert retrieved_venue.city == 'New York'
