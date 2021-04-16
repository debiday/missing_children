"""CRUD operations."""
"""CREATE. READ. UPDATE. DELETE"""


"""Making it easier to access data from DB?"""


from model import db, Child, Location, User, Tracking, connect_to_db

# <-- Children and Location  -->
def create_child(fname, lname, ethnicity, missing_age, age_2021):

    new_child = Child(fname=fname, lname=lname, ethnicity=ethnicity, missing_age=missing_age, age_2021=age_2021)

    db.session.add(new_child)
    db.session.commit()

    return new_child


def create_location(child_id, state, city, county):

    new_location = Location(child_id=child_id, state=state, city=city, county=county)

    db.session.add(new_location)
    db.session.commit()

    return new_location    


def get_child_by_id(child_id):
    """Return child details."""

    return Child.query.get(child_id)


def get_children_by_state(state):
    """Return number of children by state."""

    return Location.query.filter(Location.state == state).all()


def get_children_by_age(num):
    """Return children by missing age."""

    return Child.query.filter_by(missing_age=num).all()


def get_children_current_age(num):
    """Return children by current age."""

    return Child.query.filter_by(age_2021=num).all()


# def get_dict_children():
#     """Return a child dictionary for each child"""

#     child = {
#         'Name': fname,
#         'Missing age': age_missing,
#         'State': state 
#     }
#     return get_children()



def get_children():
    """Return all children."""

    return Child.query.all()

# <-- Users and Tracking  -->
def create_user(email, password):
    """Create and return a new user."""

    new_user = User(email=email, password=password)

    db.session.add(new_user)
    db.session.commit()

    return new_user

def create_tracking(user_id, child_id, note):
    """Create and return a new tracking."""

    new_tracking = Tracking(user_id=user_id, child_id=child_id, note=note)

    db.session.add(new_tracking)
    db.session.commit()

    return new_tracking
    

def get_users():
    """Return all users."""

    return User.query.all()

def get_user_by_id():
    """Returns user by id"""

    return User.query.get(user_id)


def get_user_by_email(email):
    """Return a user by email."""

    return User.query.filter(User.email == email).first()






if __name__ == '__main__':
    from server import app
    connect_to_db(app)
