from pydantic import BaseModel


class ArtistBase(BaseModel):
    name: str


class ArtistCreate(ArtistBase):
    pass


class ArtistResponse(ArtistBase):
    id: int
