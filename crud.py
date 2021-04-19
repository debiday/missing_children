"""CRUD operations."""
"""CREATE. READ. UPDATE. DELETE"""


"""Making it easier to access data from DB?"""


from model import db, Child, Location, User, Tracking, connect_to_db

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

    db.session.add(new_location)
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
    """Return number of children by state."""

    return Location.query.filter(Location.state == state).all()


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


def create_tracking(user_id, child_id, note):
    """Create and return a new tracking."""

    new_tracking = Tracking(user_id=user_id, child_id=child_id, note=note)

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

# <--------------------------------------------------------------->
# <Search results>
# <--------------------------------------------------------------->
# TODO: Check that this function is working
def search_db(query_terms):
    """Query database and return a list of 
       children who fit the search terms.(dict format?))"""

    new_query = []
    # Initialize with -1 for removing dupes per no. of search criteria
    num_query = -1

    if query_terms.get('fname'):
        num_query += 1
        new_query += get_child_by_fname(query_terms.get('fname'))

    if query_terms.get('lname'):
        num_query += 1
        new_query += get_child_by_lname(query_terms.get('lname'))

        # print(new_query)
    if query_terms.get('county'):
        num_query += 1
        new_query += get_child_by_county(query_terms.get('county'))

    if query_terms.get('state'):
        num_query += 1
        new_query += get_children_by_state(query_terms.get('state'))

    if query_terms.get('missing_age'):
        num_query += 1
        # print(num_query)
        # print(query_terms.get('missing_age'))
        new_query += get_children_by_age(int(query_terms.get('missing_age')))
        # print(new_query)
        # print("********")

    if query_terms.get('age_2021'):
        num_query += 1
        new_query += get_children_current_age(query_terms.get('age_2021'))

    if query_terms.get('date_missing'):
        num_query += 1
        new_query += get_children_date_missing(query_terms.get('date_missing'))
    
    print([x for x in new_query if new_query.count(x) > num_query])
    query_children = [x for x in new_query if new_query.count(x) > num_query]
    # uniqueChildren= set(new_query)
    # print(uniqueChildren)
    
    return str(query_children[:num_query+1])


# <--------------------------------------------------------------->
if __name__ == '__main__':
    from server import app
    connect_to_db(app)


