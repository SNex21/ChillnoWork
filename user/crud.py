from sqlalchemy.orm import Session
from user import auth
import user.schemas as schemas
from core import models
import random
import string

# Функция получения всех юзеров
def get_users(db: Session):
    return db.query(models.User).all()

# Функция получения юзера через имейл
def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

# Функция создание юзера
def create_user(db: Session, user: schemas.SignupModel, is_admin: bool):
    passw = user.password
    db_user = models.User(email=user.email, hashed_password=auth.encode_password(passw), is_admin=is_admin)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Функция получения всех мест
def get_places(db: Session):
    return db.query(models.Place).all()

# Функция создания места
def create_places(db: Session, place: dict, img: str):
    db_place = models.Place(
     name=place['name'],
     short_descr = place['short_descr'],
     price_from=place['price_from'],
      description=place['description'],
       lon=place['lon'],
        lat=place['lat'],
        near_city=place['near_city'],
        img=img,
        url = place['url'])
    db.add(db_place)
    db.commit()
    db.refresh(db_place)
    return db_place

# Функция получения места через его имя
def get_places_by_name(db: Session, name: str):
    return db.query(models.Place).filter(models.Place.name == name).first()

# Функция получения места через юрл
def get_place_by_url(db:Session, url: str):
    return db.query(models.Place).filter(models.Place.url == url).first()

# Функция получения части места через имя
def get_parts_by_name(db: Session, name: str):
    return db.query(models.Parts).filter(models.Parts.name == name).first()

# Функция создания части места
def create_parts(db: Session, parts: schemas.CreateParts):
    db_par = models.Parts(
    name=parts.name,
    description=parts.description,
    price=parts.price,
    place_id = parts.place_id)
    db.add(db_par)
    db.commit()
    db.refresh(db_par)
    return db_par

# Функция генерации случайной строки
def generate_random_string(length):
    letters = string.ascii_lowercase
    rand_string = ''.join(random.choice(letters) for i in range(length))
    print("Random string of length", length, "is:", rand_string)

# Тестовая функция, уже не нужна
def get_prices(place: models.Place):
    parts = place.place_parts
    a = []
    for i in range(len(parts)):
        a.insert(parts[i]['price'])
    return a

# Получение части через ид
def get_parts_by_id(db: Session, place_id: int):
    return db.query(models.Parts).filter(models.Parts.place_id == place_id).all()

# Получение картинки через её имя
def get_img_by_name(db: Session, img: str):
    return db.query(models.ListImg).filter(models.ListImg.img_url == img).first()

# получить ВСЕ картинки
def get_imgs(db: Session, place_id: int):
    return db.query(models.ListImg).filter(models.ListImg.place_id == place_id).all()

# Создать картинку
def create_img(db: Session, img_url :str, part_id: int):
    db_img = models.ListImg(
    img_url=img_url,
    part_id = part_id)
    db.add(db_img)
    db.commit()
    db.refresh(db_img)
    return db_img

# Получение id юзера через его email
def get_id_by_email(email: str, db: Session):
        user = db.query(models.User).filter(models.User.email == email).first()
        return user.id

