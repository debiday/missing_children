from flask import Flask, render_template, jsonify, request, flash, session, url_for, redirect, send_from_directory
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
        child_info_list = f"{child.fname} {child.lname}, {child.missing_age:.0f} years old.\n"
    # child_info= str(children)
        child_info_list_all += child_info_list

      return child_info_list_all
  else:
    print("Please enter a number.")

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


# TODO: Make logout button(update: logout warning for account page)
@app.route('/logout')
def logout():
    """Log user out of session."""

    del session['email']
    flash("Successfully logged out")
        
    return redirect('/')


# @app.route('/logout')
# def logout():

#     session.pop('logged_in_user_id', None)
#     flash("Successfully logged out")
        
#     return redirect('/')

# <!--------------------------------------------------------------->
# <--Routes for Tracking Child & Tracking Notes -->
# <!--------------------------------------------------------------->
@app.route('/tracking-page')
def user_page():
  """Show user's tracking-page."""
  # Removes ability to access this page if not logged in
  if 'email' in session:
    user = crud.get_user_by_email(session['email'])
    # session["email"] = email

    return render_template('tracking-page.html', user=user)
  return redirect('/')


@app.route('/search.json', methods=["POST"])
def search():
  """Search database for specific children.
    Show results matching ALL search criteria."""

  if session.get('search_query'):
    del session['search_query'] 

  session['search_query'] = {'fname': request.form.get('fname').title(),
                              'lname': request.form.get('lname').title(),
                              'county': request.form.get('county').title(),
                              'state': request.form.get('state'),
                              'missing_age': request.form.get('missing_age'),
                              'age_2021': request.form.get('age_2021'),
                              'date_missing': request.form.get('date_missing')}

  query_terms = {}
  for term in session['search_query']:
    if session['search_query'][term]:
      query_terms[term] = session['search_query'][term]

  db_matches = crud.search_db(query_terms=query_terms)

  return jsonify(db_matches)


@app.route('/child_bio', methods=['POST'])
def child_bio():
    """Show details on a particular child"""
  
    child_id = request.form.get('child_id')
    child_bio = crud.get_child_bio_by_id(child_id)

    return jsonify(child_bio)

  

# <!--------------------------------------------------------------->
# <--Routes for User Account -->
# <!--------------------------------------------------------------->
@app.route('/my-account')
def user_account():
  """Show user's account page."""
  # Removes ability to access this page if not logged in
  if 'email' in session:
    user = crud.get_user_by_email(session['email'])
    # session["email"] = email

    return render_template('my-account.html', user=user)
  return redirect('/')

# TODO: Make a conditional if tracking for child exists,
# TODO: Add notes to current tracking
@app.route('/save-tracking', methods=["POST"])
def save_tracking():
  """Saves user notes to db."""

  user_id = request.form.get('user_id')
  child_id = request.form.get('child_id')
  note = request.form.get('notes')
  date_time = request.form.get('date')


  new_tracking = crud.create_tracking(user_id, child_id, note, date_time)
  if new_tracking:
    flash("Your notes have been saved in your saved searches.")

  return "Your notes have been saved in your saved searches."
  # return redirect('/tracking-page')


@app.route('/update_tracking', methods=['POST'])
def update_tracking():
  """Update tracking from account page"""
  # print(request.form)
  note = request.form.get('note')
  tracking_id = request.form.get('tracking_id')

  crud.update_tracking(tracking_id, note)

  return redirect('/my-account')

@app.route('/delete_tracking', methods=['POST'])
def delete_tracking():
  """Delete tracking from account page"""

  tracking_id = request.form.get('tracking_id')
  crud.delete_tracking(tracking_id)
  
  return redirect('/my-account') 





if __name__ == "__main__":
    connect_to_db(app)
    app.run()
