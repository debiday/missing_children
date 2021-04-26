"""CRUD operations."""
"""CREATE. READ. UPDATE. DELETE"""


"""Making it easier to access data from DB?"""


from model import db, Child, Location, User, Tracking, connect_to_db
from datetime import datetime

# <--------------------------------------------------------------->
# <Children, Location and Note Objects>
# <--------------------------------------------------------------->

def create_child(fname, lname, ethnicity, date_missing,missing_age, age_2021):
    """Create and return a new child.
    e.g.

        >>>create_child(fname='Alex', lname='Jones', ethnicity='Hispanic', missing_age=2, age_2021=18)
        <Child name=Alex Jones missing_age=2>
    
    """

    new_child = Child(fname=fname, lname=lname, ethnicity=ethnicity, date_missing=date_missing, missing_age=missing_age, age_2021=age_2021)

    db.session.add(new_child)
    db.session.commit()

    return new_child


def create_location(child_id, state, city, county):

    new_location = Location(child_id=child_id, state=state, city=city, county=county)

    db.session.add(new_location)
    db.session.commit()

    return new_location 

# TODO: Create an update notes function?
def update_note(note):

    new_note = Users(child_id=child_id, state=state, city=city, county=county)

    db.session.add(new_note)
    db.session.commit()

    return new_location      

# <--------------------------------------------------------------->
# <Children and Location Queries>
# <--------------------------------------------------------------->

def get_child_by_id(child_id):
    """Return child details by id number."""

    return Child.query.get(child_id)


def get_child_by_fname(fname):
    """Return children by fname"""

    return Child.query.filter_by(fname=fname).all()


def get_child_by_lname(lname):
    """Return children by lname"""

    return Child.query.filter_by(lname=lname).all()


def get_child_by_county(county):
    """Return children by county"""

    return Location.query.filter_by(county=county).all()


def get_children_by_state(state):
    """Return children location by state."""

    return Location.query.filter(Location.state == state).all()

def get_location_by_id(child_id):
    """Return location details by id number."""

    return Location.query.get(child_id)


# <-----Returns children object rather than location object ----->
def get_children_from_county(county):
    """Return children by state."""

    child_query = Child.query.join(Location)
    
    return child_query.filter(Location.county == county).all()

def get_children_from_state(state):
    """Return children by state."""

    child_query = Child.query.join(Location)
    
    return child_query.filter(Location.state == state).all()
# <-----Returns children object rather than location object ----->

def get_children_by_age(missing_age):
    """Return children by missing age."""

    return Child.query.filter_by(missing_age=int(missing_age)).all()


def get_children_current_age(age_2021):
    """Return children by current age."""

    return Child.query.filter_by(age_2021=age_2021).all()


def get_children_date_missing(date):
    """Return children by date missing in format yyyy-mm-dd"""

    return Child.query.filter_by(date_missing=date).all()


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

# <--------------------------------------------------------------->
# <Setting up Users and Tracking>
# <--------------------------------------------------------------->

def create_user(email, password):
    """Create and return a new user."""

    new_user = User(email=email, password=password)

    db.session.add(new_user)
    db.session.commit()

    return new_user

# TODO: Fix and link tracking CRUD
def create_tracking(user_id, child_id, note, date_created=datetime.today()):
    """Create and return a new tracking."""

    new_tracking = Tracking(user_id=user_id, child_id=child_id, date_time=date_created, note=note)

    db.session.add(new_tracking)
    db.session.commit()

    return new_tracking
    

def get_users():
    """Return all users."""

    return User.query.all()


def get_user_by_id(user_id):
    """Returns user by id"""
    
    return User.query.get(user_id)


def get_user_by_email(email):
    """Return a user by email."""

    return User.query.filter(User.email == email).first()

# TODO: Fix get user id by email, join tracking table
def get_user_id_by_email(email):
    """Return a user id by email."""

    user_query = Tracking.query.join(User)

    return user_query.filter(User.email == email).all()

    # def get_children_from_county(county):
    # """Return children by state."""

    # child_query = Child.query.join(Location)
    
    # return child_query.filter(Location.county == county).all()

# <--------------------------------------------------------------->
# <Search results>
# <--------------------------------------------------------------->
# TODO: Check that this function is working
def search_db(query_terms):
    """Query database and return a list of 
       children who fit the search terms."""

    new_query = []
    # Initialize with -1 for removing dupes per no. of search criteria
    num_query = -1

    if query_terms.get('fname'):
        num_query += 1
        new_query += get_child_by_fname(query_terms.get('fname'))

    if query_terms.get('lname'):
        num_query += 1
        new_query += get_child_by_lname(query_terms.get('lname'))

    if query_terms.get('county'):
        num_query += 1
        new_query += get_children_from_county(query_terms.get('county'))

    if query_terms.get('state'):
        num_query += 1
        new_query += get_children_from_state(query_terms.get('state'))

    if query_terms.get('missing_age'):
        num_query += 1
        new_query += get_children_by_age(int(query_terms.get('missing_age')))

    if query_terms.get('age_2021'):
        num_query += 1
        new_query += get_children_current_age(query_terms.get('age_2021'))

    if query_terms.get('date_missing'):
        num_query += 1
        # print(num_query)
        # print(query_terms.get('date_missing'))
        new_query += get_children_date_missing(query_terms.get('date_missing'))
        # print(new_query)
        # print("********")
    
    # <-----Special scenario for only first and last name search criteria----->
    if query_terms.get('fname') and query_terms.get('lname'):
        query_children = [x for x in new_query if new_query.count(x) > num_query]
        query_children = query_children[:num_query]
        child_result = ""
        for child in query_children:
            child_result += f'<p><span id="{child.child_id}" class="child_bio">{child.fname} {child.lname}</span>' + ", missing age " + str(child.missing_age) +".</p>"
        return child_result
    if num_query > 0:
        query_children = [x for x in new_query if new_query.count(x) > num_query]
        query_children = query_children[:num_query+1]
        child_result = ""
        for child in query_children:
            child_result += f'<p><span id="{child.child_id}" class="child_bio">{child.fname} {child.lname}</span>' + ", missing age " + str(child.missing_age) +".</p>"
        return child_result
        # return str(query_children[:num_query+1])
        # This removes duplicates from the other search queries
    elif num_query == 0:
        child_result = ""
        for child in new_query:
            child_result += f'<p><span id="{child.child_id}" class="child_bio">{child.fname} {child.lname}</span>' + ", missing age " + str(child.missing_age) +".</p>"
        return child_result
    # return str(new_query)

# <--------------------------------------------------------------->
# <Individual Child(href) Search Results>
# <--------------------------------------------------------------->
def get_child_by_fname_lname(fullname):
    """Return children by both fname and lname"""
    split_str = fullname.split(" ")

    child_bio = Child.query.filter_by(fname=split_str[0]).filter_by(lname=split_str[1]).first()
    child_bio_full = {
                    'fname': child_bio.fname, 
                    'lname': child_bio.lname,
                    'date_missing': child_bio.date_missing,
                    'missing_age': child_bio.missing_age,
                    'age_2021': child_bio.age_2021,
                    'child_id': child_bio.child_id
                    }

    # Get child location from child_id, accessing location table
    location_bio = Location.query.filter_by(child_id=child_bio_full['child_id']).first()
    location_bio_full = {
                        'city': location_bio.city,
                        'county': location_bio.county,
                        'state': location_bio.state
    }

    all_info = f"Name: {child_bio_full['fname']} {child_bio_full['lname']}\n"\
               f"Missing Date: {child_bio_full['date_missing']}\n"\
               f"Missing age: {child_bio_full['missing_age']}\n"\
               f"Current Age(2021): {child_bio_full['age_2021']}\n"\
               f"City: {location_bio_full['city']}\n"\
               f"County: {location_bio_full['county']}\n"\
               f"State: {location_bio_full['state']}\n"
    # print(all_info)
    return all_info

def get_child_bio_by_id(child_id):
    """Returns child bio by child_id"""
    child = get_child_by_id(child_id)
    location = get_location_by_id(child_id)

    child_bio_full = {
                    'fname': child.fname, 
                    'lname': child.lname,
                    'date_missing': child.date_missing,
                    'missing_age': child.missing_age,
                    'age_2021': child.age_2021,
                    'child_id': child.child_id,
                    'city': location.city,
                    'county': location.county,
                    'state': location.state
                    }

    return child_bio_full

# <----------------------------SETUP----------------------------------->
if __name__ == '__main__':
    from server import app
    connect_to_db(app)


