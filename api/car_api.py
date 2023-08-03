from api import app
from fastapi import Request
from database.car_service import *


@app.get('/car/{car_id}')
async def get_exact_car(request: Request):
    data = await request.json()
    car_id = data['id']
    if car_id:
        exact_car = get_car_info(car_id)
        return {'status': 1, 'message': exact_car}
    return {'status': 0, 'message': 'неверный айди машины'}


@app.post('/add_car/')
async def add_car(car_name: str, car_model: str, car_year: int):
    if car_name and car_year and car_model:
        add = add_cars(car_name, car_model, car_year)
        return {'status': 1, 'message': add}
    return {'status': 0, 'message': 'неверно введеные данные'}


@app.delete('/car/{car_id}')
async def delete_car(request: Request):
    data = await request.json()

    car_id = data['id']
    if car_id:
        del_car = delete_cars(car_id)
        return {'status': 1, 'message': del_car}
    return {'status': 0, 'message': 'неверно веденные данные'}


