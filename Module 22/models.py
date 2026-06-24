from pydantic import BaseModel,ValidationInfo ,field_validator, constr, conint

class User(BaseModel):
    id: int
    name: str
    age: int

@field_validator('age')
def age_must_be_positive(cls,v,info: ValidationInfo):
    if v<0:
        raise ValueError('age must be positive!')
    return v

try:
    user= User(id=1,name="Alice",age=-10000)
    print(user)
except ValueError as e:
    print(e)