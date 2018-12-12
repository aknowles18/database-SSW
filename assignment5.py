import sqlite3

conn = sqlite3.connect('flowers.db')
c = conn.cursor()

def list_flowers():
    c.execute('SELECT COMNAME FROM FLOWERS')
    all_flowers = c.fetchall()
    for row in all_flowers:
        print(row)

def recent_sightings():
    ##need to replace Draperia with the flower name that the user
    ##clicked in list_flowers
    name_of_flower = ('Draperia',)
    c.execute('SELECT * FROM SIGHTINGS WHERE NAME=? ORDER BY SIGHTED DESC',
              name_of_flower)
    most_recent = c.fetchmany(10)
    for row in most_recent:
        print(row)   

def update_flowers():
    ##fill in the new_info variable with the new information 
    new_flower_info = ('','','')
    c.execute("""UPDATE FLOWERS SET GENUS=?, SPECIES=?, COMNAME=?
        WHERE COMNAME='Fireweed'""", new_flower_info)
    ##i don't think that i need a where condition because this function
    ##will only be called when it is needed?
    conn.commit()

def new_sighting():
    ##when a flower is sighted in a new place, SIGHTINGS and
    ##FEATURES should be updated with new info
    new_sightings_info = ('','','','')
    c.execute("INSERT INTO SIGHTINGS VALUES(?,?,?)", new_sightings_info)
    conn.commit()

def printer():
    c.execute("SELECT * FROM FLOWERS WHERE COMNAME='Fireweed'")
    data = c.fetchall()
    for row in data:
        print(row)



list_flowers()
##recent_sightings()
##update_flowers()
printer()


##HTML
##have to use method="post" 
##
##
##Python
##import request
##%app.route('/', methods=['POST'])??? app might be the name of file and not just a basic term
##def getvalue():
##  whatever_i_want_to_call_this_var = request.form['name']
##  probably will replace form with select
##  name will be filled with whatever i name the selection as 
##he does it with flask but
## return render_template('pass.html', n=name, age=age, dob=dob)
##then in the pass.html file:
##you can just reference it like <h1> {{n}} </h1> 
