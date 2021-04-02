"""CRUD operations."""
"""CREATE. READ. UPDATE. DELETE"""


"""Making it easier to access data from DB?"""

from model import db, Child, Location, Picture, connect_to_db

#for early stage small db testing- one state
def get_children():
    """Return all children."""

    return Child.query.all()


def get_child_by_id(child_id):
    """Return child details."""

    return Child.query.get(child_id)


def get_children_by_state(state):
    """Return number of children by state."""
    

    return Children.query.filter(location.state == state).all()

if __name__ == '__main__':
    from server import app
    connect_to_db(app)