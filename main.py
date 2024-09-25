from database import session,engine
from models.bands import Band
from models.concerts import Concert
from models.venues import Venue
from utils import get_band_concerts, get_band_venues, play_in_venue, most_performances
from models.base import Base

Base.metadata.create_all(engine)
band1 = Band("City1","NewYork")
band2 = Band("City2","Califonia")
venue1 = Venue("City1", "NewYork")
venue2 = Venue("City2 ","Califonia")

session.add_all([band1, band2, venue1, venue2])
session.commit()


play_in_venue(1, 1, "2022-01-01")
play_in_venue(1, 2, "2022-01-02")
play_in_venue(2, 1, "2022-01-03")

print(get_band_concerts(1)) 
print(get_band_venues(1))  
print(most_performances())  