"""Models for children database"""

from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()

class Child(db.Model):
    """A list of children."""

    __tablename__ = "children"

    child_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    fname = db.Column(db.String(50), nullable=False)
    lname = db.Column(db.String(50), nullable=True)
    ethnicity = db.Column(db.String(100), nullable=True)
    missing_age = db.Column(db.Integer, nullable=False)
    age_2021 = db.Column(db.Integer, nullable=False)
    # # child_id	age_2021	date_missing	lname	fname	missing_age	city	county	state	gender	ethnicity	lat	long
    # # Case Number,DLC,Last Name,First Name,Missing Age,City,County,State,Sex,Race / Ethnicity,Date Modified


    def __init__(self, child_id, age_2021, date_missing, lname, fname, missing_age, city, county, state, gender, ethnicity, lat, long):
        self.fname = fname
        self.lname = lname
        self.ethnicity = ethnicity
        self.missing_age = missing_age
        self.age_2021 = age_2021
    
    #Setting up SQLAlchemy relationship between children and locations
    location = db.relationship('Location', backref = 'children')
    
    # trackings = a list of Tracking objects
    
    def __repr__(self):
        """Provide helpful representation when printed."""

        return f"<Child child_id={self.child_id} name={self.fname} {self.lname}>"



class Location(db.Model):
    """A list of case locations."""

    __tablename__ = "locations"

    case_id = db.Column(db.Integer, db.ForeignKey('children.child_id'), autoincrement=True,  primary_key=True)
    state = db.Column(db.String(2), nullable=False)
    city = db.Column(db.String(50), nullable=False)
    county = db.Column(db.String(50), nullable=True)

    #Setting up SQLAlchemy relationship between locations and pictures
    # pictures = db.relationship('Picture', backref = 'locations')

    def __init__(self, child_id, age_2021, date_missing, lname, fname, missing_age, city, county, state, gender, ethnicity, lat, long):
    # def __init__(case_id, city, county, state):
        self.child_id = child_id
        self.state = state
        self.city = city
        self.county = county

    # children = a list of Child objects

    def __repr__(self):
        """Provide helpful representation when printed."""

        return f"<Location case_id={self.case_id} state={self.state} city={self.city}>"


class User(db.Model):
    """A list of users."""

    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement=True,  primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)


    def __init__(self, user_id, first_name, email, password):
        self.user_id = user_id
        self.first_name = first_name
        self.email = email
        self.password = password

    # trackings = a list of Tracking objects

    def __repr__(self):
        """Provide helpful representation when printed."""

        return f"<User user_id={self.user_id} lname={self.last_name} email={self.email}>"


class Tracking(db.Model):
    """A list of child records with notes."""

    __tablename__ = "trackings"

    tracking_id = db.Column(db.Integer, autoincrement=True,  primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    child_id = db.Column(db.Integer, db.ForeignKey('children.child_id'), nullable=False)
    note = db.Column(db.String(2000), nullable=True)


    def __init__(self, tracking_id, user_id, child_id, note):
        self.tracking_id = tracking_id
        self.user_id = user_id
        self.child_id = child_id
        self.note = note

    user = db.relationship('User', backref = 'trackings')
    child = db.relationship('Child', backref= 'trackings')

    def __repr__(self):
        """Provide helpful representation when printed."""

        return f"<Tracking tracking_id={self.tracking_id} child_id={self.child_id} user_id={self.user_id}>"


# class Picture(db.Model):
#     """A list of picture urls"""

#     __tablename__ = "pictures"

#     picture_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
#     pic_state = db.Column(db.String(2), db.ForeignKey('locations.state'), nullable=False)
#     picture_path = db.Column(db.String(200), nullable=False)

#     # location = backref a list of case locations.

#     def __repr__(self):
#         """Provide helpful representation when printed."""

#         return f"<Picture pic_id={self.pic_id} pic_state={self.pic_state}>"



def connect_to_db(app):
    """Connect the database to our Flask app."""

    # Configure to use our PostgreSQL database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///children'
    #postgresql setting database as name "children"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    # As a convenience, if we run this module interactively, it will leave
    # you in a state of being able to work with the database directly.

    from server import app
    connect_to_db(app)
    print("Connected to DB.")




# USERS
# -user_id (pk)
# -first name
# -last name
# -email
# -password


# TRACKINGS
# -tracking id
# -user id
# -child id
# -note 


# CHILD 

# 1. add these tables to dbdiagram.io 
# 2. create these classes in model.py 
# 3. create crud functions to instantiate a user and a tracking
# 4. create fake users using faker library and create a fake tracking record for each user 

#Create a 'create account/register' form (html)
#use /login route or you can create a new route /create_account
#in that route's view function, you will use the crud.create_user function (passing in the values from your form)
# you can utilize session and store that user's informat