#!/usr/bin/env python3
from api.base import app

@app.route('/goodbye/')
def bye():
    return {'goodbye': 'cruel world'}
