"""
    Самый лучший сервис для поиска бюджетных мест отдыха ОТДЫХАТЬнеРАБОТАТЬ
    :)
"""
# Импорт всех библиотек
import user.crud as crud
from user import auth
import user.schemas as schemas
from core.models import User
from fastapi import FastAPI, HTTPException, Form, Depends, Request, File, UploadFile, Response
from fastapi.security import HTTPBearer
from core.db import SessionLocal
from sqlalchemy.orm import Session
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from typing import List
import shutil
from PIL import Image
import os
from user.test import get_location
from typing import Union
import json
from fastapi import Cookie, FastAPI

security = HTTPBearer()


# Сессия базы данных
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Начальные настройки
templates = Jinja2Templates(directory="templates")


app = FastAPI()


app.mount("/static", StaticFiles(directory="static"), name="static")


# Получить юзеров
@app.get('/users/', response_model=List[schemas.User])
def get_users(db: Session = Depends(get_db)):
    users = crud.get_users(db)

    return users


# Функция регистрации
@app.post('/user/signup')
def signup(user: schemas.SignupModel, db: Session = Depends(get_db)):
    is_admin = True # по умолчанию не админ
    db_user = crud.get_user_by_email(db, email=user.email) # Получение юзера через его email, полученный в схеме
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered") # Рейзим ошибку, если уже есть юзер с таким email
    crud.create_user(db=db, user=user, is_admin=is_admin)

    return {'message': 'sucsessful'} # Если все ок, отправляем мэсэдж, что все классно


# функция авторизации
@app.post('/user/login')
def login(user_auth: schemas.AuthModel, db: Session = Depends(get_db),):
    user = crud.get_user_by_email(db, email=user_auth.email) # Получение юзера через его email, полученный в схеме
    if (user is None):
        return HTTPException(status_code=401, detail='Неправильный email или пароль') # Рейзим ошибку, если неправильный пароль или email
    if (not auth.verify_password(user_auth.password, user.hashed_password)):
        return HTTPException(status_code=401, detail='Неправильный Пароль или email') # Рейзим ошибку, если неправильный пароль или email
    access_token = auth.encode_token(user.email)
    refresh_token = auth.encode_refresh_token(user.email)
    content = {'access_token': access_token, 'refresh_token': refresh_token}
    response_token = JSONResponse(content=content)
    response_token.set_cookie(key="res", value=content, httponly=True)
    return response_token
  # Отправляем access и refresh токены и id пользователя, если все ок


@app.post('/user/id')
def id(user_auth: schemas.AuthModel, db: Session = Depends(get_db)):
    content = crud.get_id_by_email(db=db , email =  user_auth.email)
    response_id = JSONResponse(content=content)
    response_id.set_cookie(key="id", value=content)
    return response_id
    

# функция создания места
@app.post('/create_place')
def create_place(places: schemas.CreatePlace = Depends(), file: UploadFile = File(...), db: Session = Depends(get_db), res = Cookie(default=None),):
    if res != None:
        res = str(res)
        res=res.replace( "'",'"') 
        res = json.loads(res)
        place=places.dict() # переводим схему в словарь, для более удобного взаимодействия
        if auth.check_auth_user(res['access_token']): # если токеном все ок
            user_email = auth.decode_token(res['access_token'])
            user = crud.get_user_by_email(db = db,email = user_email['sub']) # получаем юзера через имейл, полученный в токене
            if user.is_admin: # пользователь должен быть админом
                place_db = crud.get_places_by_name(db, name=place['name'])
                if place_db: # если есть места с таким названием, то 
                    raise HTTPException(status_code=400, detail="Place already added") # рейзим ошибку
                else:
                    name, ext = os.path.splitext(file.filename)
                    while True:
                        file.filename = crud.generate_random_string(16)+ext
                        if crud.get_place_by_name_img(db, name_img=file.filename) is None:
                            break
                    with open('static/media/'+file.filename, "wb") as image: # сохраняем картинки
                        shutil.copyfileobj(file.file, image)
                    img_path = str('static/media/' + file.filename)
                    fixed_width = 1600
                    img = Image.open(img_path)
                    height_size = 1000
                    new_image = img.resize((fixed_width, height_size)) # Обрезаем картинки
                    os.remove(img_path)
                    adress = get_location(place['lat'], place['lon']) #  получение широты и долготы места для отображения на карте
                    new_image.save(img_path)

                    return crud.create_places(db=db, place=place, img = img_path, adress=adress) # создаем место, добавляя его в бд

            else:
                raise HTTPException(status_code=400, detail="You are not admin")

        else:
            raise HTTPException(status_code=400, detail="You are not auth")
    else:
        raise HTTPException(status_code=400, detail="You are not auth")        



#  создание части от места
@app.post('/create_parts')
def create_parts(parts: schemas.CreateParts ,db: Session = Depends(get_db)):
    if auth.check_auth_user(parts.token): # чекаем юзера по токену
        user_email = auth.decode_token(parts.token)
        user = crud.get_user_by_email(db = db, email = user_email['sub']) # получаем юзера через имейл, полученный из токена
        if user.is_admin: # если админ
            cat_db = crud.get_parts_by_name(db=db, name= parts.name)
            if cat_db: # если есть такая часть места
                raise HTTPException(status_code=400, detail="parts already added") # рейзим ошибку, что есть такое часть   

            return crud.create_parts(db=db, parts=parts) # иначе создаем такую часть, добавляя её в бд

        else:
             raise HTTPException(status_code=400, detail="You are not admin")
    else:
        raise HTTPException(status_code=400, detail="You are not auth")


# функция создания картинки для части места( все очень похоже описывать все не буду )
@app.post('/create_img_place')
def create_img(part_id: int, token: str, files: List[UploadFile] = File(...), db: Session = Depends(get_db)):
    if auth.check_auth_user(token):
        user_email = auth.decode_token(token)
        user = crud.get_user_by_email(db = db, email = user_email['sub'])
        if user.is_admin:
            for file in files: # через цикл прокурчиваем картинки полученные в списке и сохраняем их
                cat_db = crud.get_img_by_name(db=db, img= file.filename)
                if cat_db:
                    raise HTTPException(status_code=400, detail="img already added")

                with open('static/media/'+file.filename, "wb") as image:
                    shutil.copyfileobj(file.file, image)
                img_url = str('static/media/' + file.filename)
                crud.create_img(db=db, img_url=img_url, part_id=part_id)

            return {'message': f'Sucssesful, created {len(files)}'}

        else:
             raise HTTPException(status_code=400, detail="You are not admin")
    else:
        raise HTTPException(status_code=400, detail="You are not auth")


@app.post('/create_category')
def create_category(category: schemas.CreateCategory , db: Session = Depends(get_db),  res = Cookie(default=None)):
    if res != None:
        res = str(res)
        res=res.replace( "'",'"') 
        res = json.loads(res)
        if auth.check_auth_user(res['access_token']): # если токеном все ок
            user_email = auth.decode_token(res['access_token'])
            user = crud.get_user_by_email(db = db,email = user_email['sub']) # получаем юзера через имейл, полученный в токене
            if user.is_admin: # пользователь должен быть админом
                category_db = crud.get_category_by_name(db, name=category.name)
                if category_db: # если есть места с таким названием, то 
                    raise HTTPException(status_code=400, detail="Category already added") # рейзим ошибку
                else:
                    crud.create_category(db=db, category=category)
                    return {'message': 'Succesful, created category'}
            else:
                raise HTTPException(status_code=400, detail="You are not admin")
        else:
            raise HTTPException(status_code=400, detail="You are not auth")         


# функция обновления токена
@app.post('/refresh_token', response_model=schemas.Token)
def refresh_token(token: schemas.Token):
    new_token = auth.refresh_token(token.token)

    return new_token


# получение главной страницы
@app.get("/", response_class=HTMLResponse)
def get_main(request: Request, db: Session = Depends(get_db)):
    places = crud.get_places(db=db)

    return templates.TemplateResponse("mda.html", {"request": request, 'places':places})


# получение отдельной страницы места
@app.get("/{url}", response_class=HTMLResponse)
def get_place(url:str, request: Request, db: Session = Depends(get_db)):
    place = crud.get_place_by_url(db=db, url = url) # получение места через юрл, заданный в запросе
    location = place.adress
    parts = crud.get_parts_by_id(db = db, place_id = place.id) # получение частей места 

    return templates.TemplateResponse("place.html", {"request": request, "place": place, 'location': location, 'parts': parts}) # передача в шаблон


# получение страницы авторизации
@app.get("/user/login", response_class=HTMLResponse)
def get_main(request: Request, db: Session = Depends(get_db)):

    return templates.TemplateResponse("login.html", {"request": request})


# получение страницы регистрации
@app.get("/user/signup", response_class=HTMLResponse)
def get_main(request: Request, db: Session = Depends(get_db)):

    return templates.TemplateResponse("registration.html", {"request": request})


# получение страницы интерактивной карты
@app.get("/user/map", response_class=HTMLResponse)
def get_main(request: Request, db: Session = Depends(get_db)):

    return templates.TemplateResponse("map.html", {"request": request})


# функция получение мест и частей
@app.get("/user/places", response_model=List[schemas.Place])
def get_places(db: Session = Depends(get_db)):
    places = crud.get_places(db=db)

    return places


@app.get('/user/test')
def test(ads_id: Union[str, None] = Cookie(default=None)):
    print(ads_id)
    return {"ads_id": ads_id}



