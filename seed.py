"""Load children data into database."""

from model import Child, Location, connect_to_db, db
from server import app


#__________________________________________________#

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

    with open("data/CA.csv", encoding='utf-8-sig') as children_data:
        for r in enumerate(children_data):
            # print(r[0],r[1].split(','))
            lst = r[1].split(',')
            
            r1, r2, r3, r4, r5, r6, r7, r8, r9, r10 = lst

            db.session.add(Child(r1, r2, r3, r4, float(r5), r6, r7, r8, r9, r10))
            db.session.add(Location(int(r1), r2, r3, r4, float(r5), r6, r7, r8, r9, r10))

    db.session.commit()



#__________________________________________________#


if __name__ == '__main__':
    connect_to_db(app)
    db.create_all()

    get_children()

