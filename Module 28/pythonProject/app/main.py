from fastapi import FastAPI, HTTPException, Depends

from fastapi.security import APIKeyHeader

from pydantic import BaseModel

from typing import Optional
from dotenv import load_dotenv
import os
from database import get_db, init_db

load_dotenv()

app=FastAPI()
init_db()

api_key_header = APIKeyHeader(name="api-key")

#this next line of code allows importing the API key into main.py and checks its name#
def check_key(key:str = Depends(api_key_header)):
    allowed_keys = os.getenv("API-KEYS","").split(",")
    if not key or key not in allowed_keys:
        raise HTTPException(401,"Invalid Key, check ur pockets more")


class Item(BaseModel):
    name:str
    description:Optional[str]=None


@app.post(path="/items/", dependencies=[Depends(check_key())])
def create_items(item:Item):
    with get_db() as conn:
        cursor = conn.execute("""INSERT INTO items(name,description) VAlUES(?,?)""",
        (item.name, item.description)
        )
        return{"id":cursor.lastrowid, **item.model_dump()}
@app.get("/items/", dependencies=[Depends(check_key())])
def get_item(item_id:int):
    with get_db() as conn:
        row = conn.execute("SELECT * FROM items WHERE id=?", (item_id)).fetchone()

        if not row:
            raise HTTPException(404, "item not found")
        return [dict(row)]

    @app.put("items/{item_id}", dependencies=[Depends(check_key())])
    def update_item(item_id:int, item:Item):
        with get_db() as conn:
            cursor = conn.execute(
                """UPDATE items SET name = ? ,description=?""",(item.name,item.description,item.id)
            )
            if cursor.rowcount == 0:
                raise HTTPException (404, "no items found!")
            return {id: item_id, **item.model_dump()}
#for updating stuff#