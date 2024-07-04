# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 21:16:59 2024

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
con = sqlite3.connect('example.db')
import sqlalchemy as db
from flask_sqlalchemy import SQLAlchemy
import smtplib
from sqlalchemy import Column, Integer, DateTime
from sqlalchemy.sql import func
from sqlalchemy import Column, Integer, String, DateTime, TIMESTAMP, text

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students6.db'
db = SQLAlchemy(app)
from datetime import datetime,date

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('registrantstest.html')

if __name__ == '__main__':
   app.run(debug = False)



