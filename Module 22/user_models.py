from pydantic import BaseModel, conint, constr  #Conint and Const insure that the info will be valid  #
from typing import Optional


class User(BaseModel):
    id: int
    name: str
    age: int = 0
    email: str = ("noemail@example.com")

user1 = User(id=2, name="Axl")
print(user1)

user2 = User(id=3, name="Guy", age= 1)
print(user2)

user4 = User(id=4, name="Alice")
print(user4)

class another_user(BaseModel):
    id:conint(gt=0)
    name: constr(min_length=2, max_length=20)

valid_user = another_user(id=1, name="Alice")
print(valid_user)