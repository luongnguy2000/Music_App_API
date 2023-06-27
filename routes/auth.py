from fastapi import FastAPI, HTTPException, Depends, status, Response, APIRouter
from sqlalchemy.orm import Session
from typing import List

from services.db import get_db
from models.user import User
from schemas.user import UserLogin, UserCreate
from services.auth import (
    create_access_token,
    decode_access_token,
    get_password_hash,
    verify_password,
)
from services.send_email import send_email

router = APIRouter()


@router.post("/login/", tags=["user"])
async def login(user: UserLogin, db: Session = Depends(get_db)):
    users = db.query(User).filter(User.username == user.username).first()
    if not users:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
        )
    if not verify_password(user.password, User.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            details="Incorrect username or password",
        )
    access_token = create_access_token({"sub": user.username})
    return {"access_toke": access_token}


@router.post("/register/", tags=["user"])
async def register(user: UserCreate, db: Session = Depends(get_db)):
    users = db.query(User).filter(User.username == user.username).first()
    if users:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Username or email is valid",
        )
    db_user = User(
        username=user.username,
        email=user.email,
        password=get_password_hash(user.password),
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


@router.get("/users/me/", tags=["user"])
async def get_user_me(token: str = Depends(decode_access_token)):
    if token is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token"
        )
    username = token["sub"]
    print(username)
    return {"username": username}
