#!/usr/bin/env python3

import pytest
import sys

def test_null(app):
    assert app is not None

def test_hello(client):
    res = client.get("/hello/").get_json()
    assert res.get("hello") == "world"
