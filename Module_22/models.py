from pydantic import  BaseModel, FieldValidationInfo, field_validator,constr, conint

class User(BaseModel):
    id:int
    name:str
    age:int

    @field_validator("age")

    def age_must_be_positive(cls,v, info:FieldValidationInfo):
        if v <=0:
            raise ValueError("how did you type that if you don't exist?")
        return v

try:
    user = User(id=1,name="fishy",age=-2)
except ValueError as e :
    print(e)

class Address(BaseModel):
    street:str
    city:str
