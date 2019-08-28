""" 
============================================
; Title: donner-user-update.py
; Author: Adam Donner
; Date: 25 August 2019
; Description:  Updates email address for a
; specific record and outputs email, employee_id,
; first_name, last_name.
;===========================================
"""

from pymongo import MongoClient

import pprint

import datetime

client = MongoClient('localhost', 27017)

db = client.web335

db.users.update_one(

    {"employee_id":"0000004"},

    {
        "$set": {
            "email":"adonner@my365.bellevue.edu"
        }
    }
)



pprint.pprint(db.users.find_one({"employee_id": "0000004"}, {"_id":0, "email": 1, "employee_id": 1, "first_name": 1, "last_name": 1}))