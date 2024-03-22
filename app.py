#!/usr/bin/env python3

# Standard library imports
import datetime

# Remote library imports
from flask import request, jsonify, make_response, session
from flask_restful import Resource

# Local imports
from config import app, db, api

# Model imports
#from models import (...models) TODO

# Views
@app.route('/')
def index():
  return '<h2>CTI Training Chart API</h2>'

# TODO classes for resources

# TODO resource list

if __name__ == '__main__':
  app.run(port=5555, debug=True)