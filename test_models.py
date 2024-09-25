# tests/test_music_db.py

import pytest
from sqlalchemy import select, text
from sqlalchemy.orm import sessionmaker
from models.bands import Band
from models.concerts import Concert
from models.venues import Venue
from database import engine

@pytest.fixture
def db_session():
    # Create a new session for each test
    Session = sessionmaker(bind=engine)
    session = Session()
    yield session
    session.close()

def test_create_tables(db_session):
    # Check that the tables were created successfully
    tables = ['bands', 'concerts', 'venues']
    for table in tables:
        assert db_session.execute(text(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{table}'")).fetchone() is not None

def test_band_model(db_session):
    # Test creating a Band object
    band = Band(name='Test Band', hometown='Washington')
    db_session.add(band)
    db_session.commit()
    assert db_session.query(Band).filter_by(name='Test Band').first() is not None

def test_concert_model(db_session):
    # Test creating a Concert object
    venue = Venue( name='Test Venue', city='Alabama')
    db_session.add(venue)
    db_session.commit()
    concert = Concert( date='2023-01-01', venue_id=venue.id, band_id=1)
    db_session.add(concert)
    db_session.commit()
    assert db_session.query(Concert).filter_by(date='2023-01-01').first() is not None

def test_venue_model(db_session):
    # Test creating a Venue object
    venue = Venue(name='Test Venue', city='London')
    db_session.add(venue)
    db_session.commit()
    assert db_session.query(Venue).filter_by(name='Test Venue').first() is not None