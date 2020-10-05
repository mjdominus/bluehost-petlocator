#!/usr/bin/env python3
from api.base import app
from flask import request
from flask_api import status
from datetime import datetime
import api.exception

@app.route('/record', methods=['POST'])
def record():
    pet_id = int(request.data['pet_id'])
    when   = datetime.now()
    if "when" in request.data:
        when = datetime.fromisoformat(request.data["when"])
        if when > datetime.now():
            raise api.exception.InvalidTime(request.data["when"])
    else:
        when   = datetime.now()

    where_data = request.data['where']
    location = app.lookup_where(where_data) # not implemented

    app.location_service.record_triple(Pet(pet_id),
                                       location,
                                       when)
    # If this hadn't worked, we would have raised an exception
    # by now, so report success
    return status.HTTP_201_CREATED

@app.route('/find-pet/<int:pet_id>/<when>')
def find_pet(pet_id, when):
    res = app.location_service.find_pet_at_time(
        Pet(pet_id),
        datetime.fromisoformat(request.data["when"]))
    if res is None:
        return {}
    return res.repr()
