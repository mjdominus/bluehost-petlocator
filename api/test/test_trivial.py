#!/usr/bin/env python3

import pytest
from api import trivial

def test_null():
    assert True

def test_hello():
    assert trivial.app is not None
