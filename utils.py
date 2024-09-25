from database import session
from models.bands import Band
from models.concerts import Concert
from models.venues import Venue
from sqlalchemy.sql import func

def get_band_concerts(band_id):
    concerts = session.query(Concert).filter(Concert.band_id == band_id).all()
    return [concert.date for concert in concerts]

def get_band_venues(band_id):
    venues = session.query(Venue).join(Concert).filter(Concert.band_id == band_id).all()
    return [venue.name for venue in venues]

def play_in_venue(band_id, venue_id, date):
    band = session.query(Band).get(band_id)
    venue = session.query(Venue).get(venue_id)
    if band and venue:
        concert = Concert(band_id=band_id, venue_id=venue_id, date=date)
        session.add(concert)
        session.commit()
        return True
    else:
        return False

def most_performances():
    band_performance_counts = session.query(
        Band, func.count(Concert.id).label('performance_count')
    ).join(Concert).group_by(Band.id).order_by(func.count(Concert.id).desc()).first()
    if band_performance_counts:
        return band_performance_counts[0].name
    else:
        return None