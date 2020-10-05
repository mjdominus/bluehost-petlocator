
import pytest

import api.base
@pytest.fixture
def app():
    yield api.base.app

@pytest.fixture
def client(app):
    yield app.test_client()
