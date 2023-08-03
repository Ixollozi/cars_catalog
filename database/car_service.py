from database.models import Cars
from database import get_db

#  функция добавления машины


def add_cars(name, model, year):
    db = next(get_db())
    add = Cars(name=name, model=model, year=year)
    db.add(add)
    db.commit()
    return add.name

# функция поулчения инфы про машину


def get_car_info(car_id):
    db = next(get_db())
    get_info = db.query(Cars).filter_by(id=car_id).first()
    return get_info

# функция удаления машины


def delete_cars(car_id):
    db = next(get_db())
    del_car = db.query(Cars).filter_by(id=car_id).first()
    db.delete(del_car)
    return
