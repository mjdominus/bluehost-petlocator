#!/usr/bin/env python3
from flask_api import FlaskAPI

app = FlaskAPI(__name__)

@app.route('/hello/')
def hello():
    return {'hello': 'world'}

if __name__ == "__main__":
    app.run(debug=True)
