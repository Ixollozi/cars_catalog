from fastapi import FastAPI
from database import Base, engine
# создание таблиц в базе данных
Base = Base.metadata.create_all(bind=engine)

app = FastAPI()
from api import car_api
