# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 13:26:53 2022

1) installer falsk : 
pip install flask

2) to lauch server :
flask run
    
3) then put in your navigator
http://127.0.0.1:5000/
    

@author: CHRISTIAN
"""

from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    name = 'Max'
    return render_template('index.html', title='Welcome', username=name)

