"""Load children data into database."""

from model import Child, Location, connect_to_db, db
from server import app

from crud import create_user

import os
import crud
import model
import server

os.system('dropdb children')
os.system('createdb children')

model.connect_to_db(server.app)
model.db.create_all()

def get_children():
    """Load children from dataset into database."""

    with open("data/finaldata.csv", encoding='utf-8-sig') as children_data:
        for r in enumerate(children_data):
            data = r[1].split(',')
            child_id, age_2021, date_missing, lname, fname, missing_age, city, county, state, gender, ethnicity, latitude, longitude = data

            child_instance = crud.create_child(fname=fname, lname=lname, ethnicity=ethnicity, missing_age=int(missing_age), age_2021=int(age_2021))
            
            location_instance = crud.create_location(child_id=child_instance.child_id, state=state, city=city, county=county)

            # print(location_instance)
            # print(location_instance.child_id)


if __name__ == '__main__':
    connect_to_db(app)
    db.create_all()

    get_children()

