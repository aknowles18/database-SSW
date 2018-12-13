from flask import Flask, render_template, request, g
import sqlite3

app = Flask (__name__)

# conn = sqlite3.connect('flowers.db')
# c = conn.cursor()

DATABASE = 'flowers.db'

def get_db():
  db = getattr(g, '_database', None)
  if db is None:
      db = g._database = sqlite3.connect(DATABASE)
  return db

@app.teardown_appcontext
def close_connection(exception):
  db = getattr(g, '_database', None)
  if db is not None:
      db.close()

@app.route('/')
def index():
  c = get_db().cursor()
  c.execute('SELECT COMNAME FROM FLOWERS')
  all_flowers = c.fetchall()
  return render_template("index.html", all_flowers=all_flowers)



@app.route('/update', methods = ['POST', 'GET'])
def update():
  # this just gets the data from the db
  c = get_db().cursor()
  c.execute('SELECT GENUS, SPECIES, COMNAME FROM FLOWERS')
  genus_flowers = c.fetchall()

  # if request.method =='POST':
  #   result = request.form
  #   return render_template("update.html", result=result, genus_flowers=genus_flowers)
  #   # return redirect(url_for('update'))
  # else:
  return render_template("update.html", genus_flowers=genus_flowers)




@app.route('/update2', methods = ['POST', 'GET'])
def update2():
  if request.method =='POST':
    result = request.form
    # get the results from the form
    gen_result = request.form['genus']
    spec_result = request.form['species']
    com_result = request.form['comname']

    # allows me to interact with the db
    c = get_db().cursor()
    # puts the form results into an array that can be accessed by the sqlite (replaces the ?)
    new_flower_info = (gen_result, spec_result, com_result)




    # this works so long as you are replacing fremontodendron
    c.execute(""" UPDATE FLOWERS SET GENUS=?, SPECIES=?, COMNAME=? WHERE GENUS='?'""", new_flower_info)

    # ask for the db like normal to send to the HTML doc
    c.execute('SELECT GENUS, SPECIES, COMNAME FROM FLOWERS')
    genus_flowers = c.fetchall()
    # return render_template("update2.html", genus_flowers=genus_flowers)
    return render_template("update2.html" , result=result, genus_flowers=genus_flowers)
  else:
    return render_template("update.html")





























# @app.route('/result', methods = ['POST', 'GET'])
# def result():
#   if request.method =='POST':
#     result = request.form
#     return render_template("result.html", result=result)


@app.route('/insert')
def insert():
  c = get_db().cursor()
  # this just gets the data from the db

  c = get_db().cursor()
  c.execute('SELECT NAME, PERSON, LOCATION, SIGHTED FROM SIGHTINGS')
  sighting_flowers = c.fetchall()
  return render_template("insert.html", sighting_flowers=sighting_flowers)

@app.route('/query')
def query():
  c = get_db().cursor()
  # this just gets the data from the db

  c.execute('SELECT NAME FROM SIGHTINGS')
  name_flowers = c.fetchall()
  return render_template("query.html", name_flowers=name_flowers)

  c.execute('SELECT NAME, SIGHTED FROM SIGHTINGS')
  sighting_flowers = c.fetchall()
  return render_template("query.html", sighting_flowers=sighting_flowers)

@app.route('/profile/<name>')
def profile(name):
  return render_template("profile.html", name=name)


if __name__ == "__main__":
  app.run(debug=True)