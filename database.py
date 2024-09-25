from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from models.bands import Band
from models.concerts import Concert
from models.venues import Venue

engine = create_engine('sqlite:///music.db')


Session = sessionmaker(bind=engine)
session = Session()