#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 10:26:23 2018

@author: halilbayraktar
"""

from flask import Flask, render_template

appa = Flask(__name__)

@appa.route('/')
def index():
    return render_template('registrants.html')


#@app.route('/user/<name>')
#def user(name):       
 #       return render_template('user.html', name=name)



if __name__ == '__main__':
    appa.run(debug=False)

