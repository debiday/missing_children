"""CRUD operations."""
"""CREATE. READ. UPDATE. DELETE"""


"""Making it easier to access data from DB?"""


# for early stage small db testing- one state


from model import db, Child, Location, connect_to_db
def get_children():
    """Return all children."""

    return Child.query.all()


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

if __name__ == '__main__':
    from server import app
    connect_to_db(app)
