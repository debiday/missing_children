from flask import Flask, render_template, jsonify, request, flash, session, url_for, redirect
from model import db, connect_to_db
from jinja2 import StrictUndefined
from markupsafe import escape
import crud

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined

# <!--------------------------------------------------------------->
# <-- Routes for homepage -->
# <!--------------------------------------------------------------->
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
  child_info_list = ""


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


# <!--------------------------------------------------------------->
# <--Routes for User -->
# <!--------------------------------------------------------------->
@app.route('/registration')
def show_registration():
    """Show registration page."""

    return render_template("registration.html")



@app.route('/newusers', methods = ["POST"])
def register_user():
  """Saves user information to database"""

# TODO: Verify email format
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
  

@app.route('/login', methods = ['POST'])
def submit_login_form():
  """Submits the login form."""

  user = crud.get_user_by_email(request.form['email'])
  password = request.form['password']

  if user == None:
    flash('''An account for this email doesn't exist yet.
              Please create a new account.''')
    return redirect('/')
  elif password != user.password:
    flash('Wrong password. Please try again.')
    return redirect('/')

  else: 
    flash('Logged in!')
    session['email'] = user.email

    return redirect('/tracking-page')


# TODO: Make logout button
@app.route('/logout')
def logout():
    """Log user out of session."""

    del session['email']
    flash("Successfully logged out")
        
    return redirect('/')


# <!--------------------------------------------------------------->
# <--Routes for Tracking -->
# <!--------------------------------------------------------------->
@app.route('/tracking-page')
def user_page():
  """Show user's tracking-page."""
# TODO: Remove ability to access this page if not logged in

  if 'email' in session:
    user = crud.get_user_by_email(session['email'])
    # session["email"] = email

    return render_template('tracking-page.html', user=user)
  return redirect('/')

# TODO: Create link from browser to db
@app.route('/search.json', methods=["POST"])
def search():
  """Search database for specific children.
    Show results matching ALL search criteria."""

  if session.get('search_query'):
    del session['search_query'] 
    # Clears all fields?

  session['search_query'] = {'fname': request.form.get('fname'),
                              'lname': request.form.get('lname'),
                              'county': request.form.get('county'),
                              'state': request.form.get('state'),
                              'missing_age': request.form.get('missing_age'),
                              'age_2021': request.form.get('age_2021'),
                              'date_missing': request.form.get('date_missing')}

# History table that includes the user_id, time stamp, string 250? Maybe json array?

  query_terms = {}
  for term in session['search_query']:
    if session['search_query'][term]:
      query_terms[term] = session['search_query'][term]

  db_matches = crud.search_db(query_terms=query_terms)
  print("*******")
  print(type(db_matches))

# TODO: Print something to screen
  # db_matches_dict = {}
  # for child in db_matches:
  #   db_matches_dict[child.child_id] = {'fname': child.fname, 
  #                                     'lname': child.lname}

  return jsonify(db_matches)

@app.route('/child_bio', methods=['POST'])
def child_bio():
    """Show details on a particular exercise"""
  
    child_id = request.form.get('child_id')
    child_bio = crud.get_child_bio_by_id(child_id)

    return jsonify(child_bio)








if __name__ == "__main__":
    connect_to_db(app)
    app.run(debug=True, host='0.0.0.0')
