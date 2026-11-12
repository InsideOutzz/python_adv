from pydantic import BaseModel

class ArtPieceBase(BaseModel):
    title:str
    artist_id:int
    art_piece_link:str = ""
    published_year:int | None = None

class ArtPieceCreate(ArtPieceBase):
    pass
class ArtPieceResponse(ArtPieceBase):
    id:int