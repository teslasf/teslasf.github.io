# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 10:51:55 2021

@author: 90539
"""
import random
from datetime import date,datetime
from flask import Flask, request, flash, url_for, redirect, render_template
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from flask import Flask
from sqlalchemy import Column, String
from sqlalchemy import *
#from sqlalchemy.orm import relation, sessionmaker
from sqlalchemy import Column, Integer, String
import sqlite3
import sqlalchemy as db
from flask_sqlalchemy import SQLAlchemy
import smtplib
from sqlalchemy import Column, Integer, DateTime
from sqlalchemy.sql import func
from sqlalchemy import Column, Integer, String, DateTime, TIMESTAMP, text

con = sqlite3.connect('example.db')
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students6.db'
db = SQLAlchemy(app)
from datetime import datetime,date


#Base = declarative_base()

class students6(db.Model):
    id = db.Column('student_id', db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    lastname = db.Column(db.String(100))
   #email = db.Column(db.String(100))
    sport = db.Column(db.String(100))
    id2 = db.Column('id2a',db.Integer())


    def __init__(self, name,lastname, sport,id2):
        self.name = name
        self.lastname = lastname
        self.sport = sport
        self.id2=id2



REGISTRANTS = {}
SPORTS = [
    "Dodgeball",
    "Flag Football",
    "Soccer",
    "Volleyball",
    "Ultimate Frisbee"
]




@app.route("/")
def index():
    return render_template("registrants.html", sports=SPORTS, students6 = students6.query.all())

@app.route("/register", methods = ['GET', 'POST'])
def register():
    id2=random.randint(5,45)
    #name = request.form.get("name")
    # if not name:
        # return render_template("error.html", message="Missing name")

    #sport = request.form.get("sport")
    # if not sport:
    #     return render_template("error.html", message="Missing sport")
    # if sport not in SPORTS:
    #     return render_template("error.html", message="Invalid sport")

    if request.method == 'POST':
        if not request.form['name']:
            error_statement="all forms fields are required"
            return render_template("fail.html",error=error_statement)
            #flash('Please enter all the fields', 'error')
                  
        else:
         
            name = request.form.get("name")
            lastname = request.form.get("lastname")
            sport = request.form.get("sport")
           
          
            
            if not name or not lastname or not sport:
                error_statement="all forms fields are required"
                return render_template("fail.html",error=error_statement)
            
            
            
            student = students6(request.form['name'],request.form['lastname'],request.form['sport'],id2)
            print ("Creating database tablessss...")
            db.session.add(student)
            db.session.commit()
         
          
    REGISTRANTS[name] = [lastname, sport,id2*100]
    #db.execute("INSERT INTO registrants000......................................................................................................... (name, sport) VALUES(?, ?)", name, sport)
    
    return redirect("/registrants")


@app.route("/subscribe")
def subscribe():
    title="Subscribe yo my email newsletter"
    return render_template("subscribe.html", title=title)

@app.route("/contact")
def contact():
    return render_template("contact.html",sports=SPORTS, students6 = students6.query.all() )


@app.route("/registrants")
def registrants():
    
    
    return render_template("registrants.html", registrants=REGISTRANTS)


@app.route("/about")
def about():
    return render_template("about.html")

# @app.route("/", methods=["GET", "POST"])
# def index():
#     if request.method == "POST":
#         return render_template("greet.html", name=request.form.get("name", "world"))
#     return render_template("index3.html")



@app.route('/regi', methods=['GET', 'POST'])
def regirt():
    return render_template("registrants.html")
 


@app.route('/cool_form', methods=['GET', 'POST'])
def cool_form():
    if request.method == 'POST':
        # do stuff when the form is submitted

        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else
        return redirect(url_for('index'))
    return render_template('index3.html')




#@app.route("/greet")
@app.route("/greet",methods=["POST"])
def greet():
    #return render_template("greet.html", name=request.args.get("name", "world"))
    return render_template("greet.html", name=request.form.get("name", "world"))








if __name__ == "__main__":
#    db.create_all()
    app.run(debug=False)