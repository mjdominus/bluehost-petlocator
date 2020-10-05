#!/usr/bin/env python3

import pytest
import sys

from locator.storage import LocationStorage
from locator.service import LocationAPI

def test_init():
    with pytest.raises(TypeError):
        s = LocationAPI()

    stor = LocationStorage()
    s = LocationAPI(stor)

    assert True
