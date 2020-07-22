import pytest
# testing our flask app
from urlshort import create_app

@pytest.fixture
def app():
    app = create_app()
    yield app

# creating another fixture to get a client
# testing framework can act as if it was a browser and testing out the project for us
@pytest.fixture()
def client(app):
    return app.test_client()