from email.policy import default
from enum import unique
from  core.db import Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Boolean
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(100), unique=True, index=True)
    hashed_password = Column(String(100))
    is_admin = Column(Boolean, default=False)


class Place(Base):
    __tablename__ = 'place'

    id = Column(Integer, primary_key=True, unique=True)
    name = Column(String(150), unique=True)
    short_descr  = Column(String(35))
    price_from = Column(Integer)
    description = Column(String(1000))
    img = Column(String(200))
    lat = Column(Float, unique=True)
    lon = Column(Float, unique=True)
    adress=Column(String(200), unique=True)
    near_city = Column(String(100))
    url = Column(String(100), unique = True)
    category_id = Column(Integer, ForeignKey("place_category.id"))


    place_parts = relationship("Parts")


class Parts(Base):
    __tablename__ = 'parts'

    id = Column(Integer, primary_key=True, unique=True)
    name = Column(String(100), unique=True)
    description = Column(String(1000))
    price = Column(Integer)
    
    img_list = relationship("ListImg")
    place_id = Column(Integer, ForeignKey("place.id"))
    

class RefreshToken(Base):
    __tablename__ = 'refresh_token'

    id = Column(Integer, primary_key=True, unique=True)
    value = Column(String(200))


class ListImg(Base):
    __tablename__='listimg'

    id = Column(Integer, primary_key=True, unique=True)
    img_url = Column(String(100))
    
    part_id = Column(Integer, ForeignKey("parts.id"))


class PlaceCategory(Base):
    __tablename__='place_category'

    id = Column(Integer, primary_key=True, unique=True)
    name = Column(String(100), unique=True)
    place = relationship("Place")