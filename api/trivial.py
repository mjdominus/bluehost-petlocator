#!/usr/bin/env python3
from api.base import app

@app.route('/hello/')
def hello():
    return {'hello': 'world'}
