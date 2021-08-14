import pytest
from app import create_app
from app.models import User


@pytest.fixture(scope='module')
def new_user():
    user = User(name='God', email_address='god@heaven.com')
    return user

@pytest.fixture(scope='module')
def test_client():
    app = create_app('config.TestConfig')
    with app.test_client() as testing_client:
        with app.app_context():
            yield testing_client

def test_user(new_user):
    assert new_user.name == 'God'
    assert new_user.email_address == 'god@heaven.com'

def test_home_page(test_client):
    response = test_client.get('/')
    assert response.status_code == 200
    assert b"Hello" in response.data