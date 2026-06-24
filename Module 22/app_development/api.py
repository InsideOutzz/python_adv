from pydantic import BaseModel
from fastapi import FastAPI

app = FastAPI()

class User(BaseModel):
    id: int
    name: str
    age: int
    email: str

class Person(BaseModel):
    name: str
    age: int

class PersonResponse(BaseModel):
    message: str

@app.post("/users/")
async def user_post(user: User):
    return user

@app.post("/create_person/", response_model=PersonResponse)
async def create_person(person: Person):
    return {"message": f"Person {person.name} created with age {person.age}"}
