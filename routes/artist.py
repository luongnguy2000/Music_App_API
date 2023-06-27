from fastapi import FastAPI, HTTPException, Depends, status, Response, APIRouter
from sqlalchemy.orm import Session
from typing import List

from config.db import get_db
from models.models import Artist
from schemas.artist import Artists, ArtistCreated
from services.auth import (
    create_access_token,
    decode_access_token,
    get_password_hash,
    verify_password,
)
from services.send_email import send_email

artist_router = APIRouter()


@artist_router.get("/artists/", response_model=List[Artists])
async def get_all_artists(skip: 0, limit: int = 100, db: Session = Depends(get_db)):
    artists = db.query(Artist).offset(skip).limit(limit).all()
    return artists


@artist_router.post("/artists/")
async def create_artists(artist: ArtistCreated, db: Session = Depends(get_db)):
    artists = db.query(Artist).filter(Artist.name == artist.name).first()
    if artists:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
        )
    db_artist = Artist(name=artist.name, bio=artist.bio, image_url=artist.image_url)
    db.add(db_artist)
    db.commit()
    db.refresh(db_artist)
    return db_artist
