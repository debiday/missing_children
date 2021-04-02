"""Load children data into database."""

from model import Child, connect_to_db, db
from server import app


#__________________________________________________#

# import os
# import crud
# import model
# import server

# os.system('dropdb children')
# os.system('createdb children')

# model.connect_to_db(server.app)
# model.db.create_all()

def get_children():
    """Load children from dataset into database."""

    with open("data/CA.csv") as children_data:
        for r in enumerate(children_data):
            # print(r[0],r[1].split(','))
            lst = r[1].split(',')
            #print(r[1].split(','))
            for i in lst:
                if i == 0:
                    pass
                else: 
                    lst[4] = float(lst[4])
            return lst
            
            r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11 = lst
            print(type(r5))

            db.session.add(Child(r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11))

    db.session.commit()

#__________________________________________________#

if __name__ == '__main__':
    connect_to_db(app)
    db.create_all()

    get_children()

