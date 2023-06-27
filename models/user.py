from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String)
    email = Column(String)
    password = Column(String)
    date_created = Column(DateTime)


class Artist(Base):
    __tablename__ = "artists"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    bio = Column(String)
    image_url = Column(String)
    date_created = Column(DateTime)


class Album(Base):
    __tablename__ = "albums"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    artist_id = Column(Integer, ForeignKey("artists.id"))
    release_date = Column(DateTime)
    image_url = Column(String)
    date_created = Column(DateTime)

    artist = relationship("Artist", backref="albums")


class Track(Base):
    __tablename__ = "tracks"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    album_id = Column(Integer, ForeignKey("albums.id"))
    duration = Column(Integer)
    track_number = Column(Integer)
    date_created = Column(DateTime)

    album = relationship("Album", backref="tracks")
