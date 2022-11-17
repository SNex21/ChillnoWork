from pydantic import BaseModel
from typing import List
import user

# Схема авторизации
class AuthModel(BaseModel):
    email: str
    password: str

# Схема регистрации
class SignupModel(AuthModel):
    pass

# Схема части места 
class Parts(BaseModel):
    name: str
    description: str
    price: int

    class Config:
        orm_mode = True

# Схема места
class Place(BaseModel):
    id: int
    name: str
    short_descr: str
    price_from: int
    description: str
    lat: float
    lon:float
    near_city: str
    url: str
    img: str
    place_parts: List[Parts] = []

    class Config:
        orm_mode = True

# Схема создания места
class CreatePlace(BaseModel):
    name: str
    short_descr: str
    price_from: int
    description: str
    lat: float
    lon:float
    near_city: str
    url: str
    category_id: int

    class Config:
        orm_mode = True

# Схема юзера
class User(BaseModel):
    id: int
    email:str
    is_admin: bool

    class Config:
        orm_mode = True

# схема токена
class Token(BaseModel):
    token: str


class DecodeToken(BaseModel):
    decode_token:str

# Схема создания части места 
class CreateParts(BaseModel):
    token: str
    name: str
    description: str
    price: int
    place_id: int

    class Config:
        orm_mode = True


class CreateCategory(BaseModel):
    name: str

    class Config:
        orm_mode = True


