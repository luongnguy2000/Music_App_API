from pydantic import BaseModel


class Artists(BaseModel):
    name: str
    bio: str | None
    image_url: str | None


class ArtistCreated(BaseModel):
    name: str
    bio: str | None
    image_url: str | None
