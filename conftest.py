
import pytest
from api import trivial

@pytest.fixture
def app():
    yield trivial.app

@pytest.fixture
def client(app):
    yield app.test_client()
