from flask import Flask, render_template, jsonify, request, flash, session, url_for, redirect
from model import db, connect_to_db
from jinja2 import StrictUndefined
from markupsafe import escape
import crud

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined

# @app.route('/')
# def index ():
#   if 'username' in session:
#     return 'Logged in as %s' escape(session['username'])
#   return 'You are not logged in'

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#   # uses wtfforms custom loginform to validate?
#   form = LoginForm()
#   if form.validate_on_submit():
#     login_user(user)

#     flask.flash('Logged in successfully.')
#     next = flask.request.args.get('next')

#     if not is_safe_url(next):
#       return flask.abort(400)

#     return flask.redirect(next or flask.url_for('index'))
#   return flask.render_template('homepage.html', form=form)

# @app.route('/logout')
# def logout():
#   #remove the username form the session if it's there
#   session.pop('username', None)
#   return redirect(url_for('index'))


  


@app.route('/age')
def same_age():
  """Return children dictionary for users age"""

  age = request.args.get("user-age")

  child_info= {}
  child_info_list_all = ""

  if age.isdigit():
    children = crud.get_children_current_age(age)
    for i in range(len(children)): 
      for child in children:
        child_info = { "fname":child.fname,
                       "lname": child.lname, 
                      "missing_age":int(child.missing_age),
                     }              
        child_info_list = f"{child.fname} {child.lname}, {child.missing_age:.0f} years old. "
    # child_info= str(children)
        child_info_list_all += child_info_list

      return child_info_list_all
  else:
    print("Please enter a number.")


    # for i, child in enumerate(children):
    #   for i in range(len(children)):
    #     child_info = { "fname":child.fname, 
    #                 "age":child.age_2021 }
    #    // TODO: Figure out how to index into dict
    #     child_info_list += child_info.fname + "\n"

    # for child in children:
    #   child_info = { "fname":child.fname, 
    #                 "age":child.age_2021 }

  return child_info_list
  # return "HI"


@app.route('/')
def show_homepage():
    """Show the homepage."""

    return render_template("homepage.html")

@app.route('/test')
def all_children():
    """View all children."""

    children = crud.get_children()

    return render/_template('test.html', children=children)

# @app.route('/test.json')
# def all_children_json():
#   """Return a child dictionary for each child"""

#     child = crud.get_children()
  
#     return jsonify([{"name":"Kat"}])
# # children into dictionary
# """
# crud:
# 1. query for children
# 2. loop over each child and make a dictionary 
#     (something like {"name":child.name, "age":child.age})
#     add each child dict into a list
# server.py:
# 3. jsonify the list of child dicts and send that to the front end
# 4. create js file (check script for jquery $.get(url))
# """




if __name__ == "__main__":
    connect_to_db(app)
    app.run(debug=True, host='0.0.0.0')
