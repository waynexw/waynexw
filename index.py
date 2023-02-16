# indivi Homepage -  https://waynexw.github.io/
  
import os
import uuid
import json  
import pymysql  # installing pymysql firstly requeried-wayne W
import mysql.connector 
from datetime import datetime, timedelta
from flask import jsonify, abort, request, Blueprint
from validate_email import validate_email

REQUEST_API = Blueprint('request_api', __name__)

def get_blueprint():
    """Return the blueprint for the main app module"""
    return REQUEST_API

# Decide to use json or MySQL database - wayneW.
with open("./routes/env_conf.json", 'r', encoding='utf-8') as ec:
    json_data = json.load(ec)
  # print(json_data)
# DB_TYPE = json_data['DB_TYPE']

DB_TYPE = str(os.getenv('dbtype')) # use env viriables to set DB_TYPE
DB_TYPE = os.getenv('dbtype')
