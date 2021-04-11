from flask import Flask, render_template, jsonify, request, flash, session, redirect
from model import db, connect_to_db
from jinja2 import StrictUndefined
import crud

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined


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
                      "missing_age":child.missing_age }
        child_info_list = str(child.fname) + " " + str(child.missing_age)+ "\n"
    # child_info= str(children)
        child_info_list_all += child_info_list

    return child_info_list_all


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
