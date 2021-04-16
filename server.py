from flask import Flask, render_template, jsonify, request, flash, session, url_for, redirect
from model import db, connect_to_db
from jinja2 import StrictUndefined
from markupsafe import escape
import crud

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined


# <-- Routes for homepage -->
@app.route('/')
def show_homepage():
    """Show the homepage."""

    return render_template("homepage.html")

# @app.route('/test')
# def all_children():
#     """View all children."""

#     children = crud.get_children()

#     return render/_template('test.html', children=children)

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
                      "missing_age":child.missing_age,
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

    #     child_info_list += child_info.fname + "\n"

    # for child in children:
    #   child_info = { "fname":child.fname, 
    #                 "age":child.age_2021 }

  return child_info_list

# <--Routes for user and tracking -->

@app.route('/registration')
def show_registration():
    """Show registration page."""

    return render_template("registration.html")



@app.route('/newusers', methods = ["POST"])
def register_user():
  """Saves user information to database"""

  email = request.form.get('email')
  password = request.form.get('password')

  user = crud.get_user_by_email(email)

  if user: 
    flash('Email is already in use. Please log in.')
  else:
    user = crud.create_user(email, password)
    session["email"] = email
    flash('Your account has been created! Please log in.')

  return redirect('/')


@app.route('/tracking-page')
def user_page():
  """Show user's tracking-page."""
# TODO: Remove ability to access this page if not logged in
  if 'email' not in session:
    return redirect("/")

  if 'email' in session:
    user = crud.get_user_by_id(session['user_id'])
    # session["email"] = email

  return render_template('tracking-page.html', user=user)
  


@app.route('/login', methods = ['POST'])
def submit_login_form():
  """Submits the login form."""

  user = crud.get_user_by_email(request.form['email'])

  password = request.form['password']

  if user == None:
    flash('''An account for this email doesn't exist yet.
              Please create a new account.''')
  elif password != user.password:
    flash('Wrong password. Please try again.')
    return redirect('/')

  else: 
    flash('Logged in!')
    session['user_id'] = user.user_id

  return redirect('/tracking-page')


if __name__ == "__main__":
    connect_to_db(app)
    app.run(debug=True, host='0.0.0.0')
