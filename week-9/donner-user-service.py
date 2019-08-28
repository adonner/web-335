""" 
============================================
; Title: donner-user-service.py
; Author: Adam Donner
; Date: 25 August 2019
; Description:  Querying and creating documents
; in a MongoDB database through Python and pymongo.
;===========================================
"""

from pymongo import MongoClient

import pprint

import datetime

client = MongoClient('localhost', 27017)

db = client.web335

user = {

    "first_name": "Claude",
    "last_name": "Debussy",
    "email": "cdebussy@me.com",
    "employee_id": "0000004",
    "date_created": datetime.datetime.utcnow()
}

user_id = db.users.insert_one(user).inserted_id

print(user_id)

pprint.pprint(db.users.find_one({"employee_id": "0000004"}))