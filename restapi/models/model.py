from pydantic import BaseModel

class Address(BaseModel):
    HouseNumber: str
    Locality: str
    AreaCode: int
    CityName: str
    State: str
    Country: str
    ContactNumber: int
    